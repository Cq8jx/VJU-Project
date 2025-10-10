/**
 * Google Form generator from Excel definitions.
 *
 * This script reads form definitions from a Google Sheets workbook and
 * creates/updates Google Form items. When the automation stops for any
 * reason, it sends a notification email that now includes a detailed
 * execution log together with a snapshot of key variables.
 */

/**
 * Entry point for the trigger.
 */
function createGoogleFormFromExcel() {
  const context = createExecutionContext_('Google Form from Excel automation');
  let config;

  try {
    config = loadConfiguration_(context);
    context.capture('config', config);

    const spreadsheet = SpreadsheetApp.openById(config.sourceSpreadsheetId);
    context.capture('spreadsheetName', spreadsheet.getName());

    const sheet = spreadsheet.getSheetByName(config.sheetName);
    if (!sheet) {
      throw new Error('Sheet "' + config.sheetName + '" was not found.');
    }

    const lastRow = sheet.getLastRow();
    const lastColumn = sheet.getLastColumn();
    context.capture('lastRow', lastRow);
    context.capture('lastColumn', lastColumn);

    if (lastRow <= 1) {
      context.log('No form definitions found in the sheet.');
      return;
    }

    const form = FormApp.openById(config.formId);
    context.capture('formTitle', form.getTitle());

    const dataRange = sheet.getRange(2, 1, lastRow - 1, lastColumn);
    const records = dataRange.getValues();
    context.capture('recordsCount', records.length);

    records.forEach(function (row, index) {
      const record = mapRowToRecord_(row, config.headers);
      context.capture('currentRecord', record);
      context.log('Processing form item', {
        rowNumber: index + 2,
        type: record.type,
        title: record.title
      });
      upsertFormItem_(form, record, context);
    });

    context.log('Form update completed successfully.');
  } catch (error) {
    context.log('Processing aborted due to error.', {
      message: error && error.message,
      stack: error && error.stack
    });
    notifyFailure_(error, context, config);
    throw error;
  }
}

/**
 * Creates a structured execution context used for logging and capturing variables.
 *
 * @param {string} processName
 * @return {{log: function(string, Object=): void, capture: function(string, *): *, snapshot: function(): Object}}
 */
function createExecutionContext_(processName) {
  const startTime = new Date();
  const logs = [];
  const variables = {};

  return {
    log: function (message, details) {
      const entry = {
        time: new Date(),
        message: message,
        details: details || null
      };
      logs.push(entry);
      if (details) {
        Logger.log(message + '\n' + safeStringify_(details));
      } else {
        Logger.log(message);
      }
    },
    capture: function (name, value) {
      variables[name] = value;
      return value;
    },
    snapshot: function () {
      return {
        processName: processName,
        startTime: startTime,
        endTime: new Date(),
        logs: logs.slice(),
        variables: Object.assign({}, variables)
      };
    }
  };
}

/**
 * Loads configuration from Script Properties.
 *
 * Required properties:
 *   - SOURCE_SPREADSHEET_ID
 *   - SOURCE_SHEET_NAME (defaults to "FormItems")
 *   - TARGET_FORM_ID
 *   - ALERT_RECIPIENTS (comma separated)
 *
 * @param {Object} context
 * @return {{sourceSpreadsheetId: string, sheetName: string, formId: string, headers: Array<string>, recipients: Array<string>}}
 */
function loadConfiguration_(context) {
  const props = PropertiesService.getScriptProperties();
  const recipients = (props.getProperty('ALERT_RECIPIENTS') || '')
    .split(',')
    .map(function (email) { return email.trim(); })
    .filter(Boolean);

  const config = {
    sourceSpreadsheetId: props.getProperty('SOURCE_SPREADSHEET_ID'),
    sheetName: props.getProperty('SOURCE_SHEET_NAME') || 'FormItems',
    formId: props.getProperty('TARGET_FORM_ID'),
    headers: JSON.parse(props.getProperty('FORM_HEADERS_JSON') || '[]'),
    recipients: recipients
  };

  if (!config.sourceSpreadsheetId) {
    throw new Error('Script property SOURCE_SPREADSHEET_ID is not configured.');
  }

  if (!config.formId) {
    throw new Error('Script property TARGET_FORM_ID is not configured.');
  }

  if (!config.recipients.length) {
    throw new Error('Script property ALERT_RECIPIENTS is not configured.');
  }

  return config;
}

/**
 * Converts a spreadsheet row into a record object.
 *
 * @param {Array<*>} row
 * @param {Array<string>} headers
 * @return {Object}
 */
function mapRowToRecord_(row, headers) {
  if (!headers || !headers.length) {
    return {
      type: row[0],
      title: row[1],
      helpText: row[2],
      choices: row[3],
      required: row[4]
    };
  }

  return headers.reduce(function (accumulator, header, index) {
    accumulator[header] = row[index];
    return accumulator;
  }, {});
}

/**
 * Creates or updates a form item based on the supplied record.
 *
 * @param {FormApp.Form} form
 * @param {Object} record
 * @param {Object} context
 */
function upsertFormItem_(form, record, context) {
  if (!record || !record.type || !record.title) {
    context.log('Skipping row because mandatory fields are missing.', record);
    return;
  }

  switch (String(record.type).toLowerCase()) {
    case 'multiplechoice':
    case 'multiple choice':
      upsertMultipleChoiceItem_(form, record, context);
      break;
    case 'checkbox':
    case 'checkboxes':
      upsertCheckboxItem_(form, record, context);
      break;
    case 'paragraph':
      upsertParagraphItem_(form, record);
      break;
    case 'text':
    case 'shortanswer':
    case 'short answer':
      upsertTextItem_(form, record);
      break;
    default:
      context.log('Unsupported question type. Row skipped.', record);
  }
}

function upsertMultipleChoiceItem_(form, record, context) {
  const item = findItemByTitle_(form, record.title) || form.addMultipleChoiceItem();
  item.setTitle(record.title);
  item.setHelpText(record.helpText || '');
  item.setChoiceValues(parseChoiceValues_(record.choices));
  item.setRequired(Boolean(record.required));
  context.log('Multiple choice item updated.', { title: record.title });
}

function upsertCheckboxItem_(form, record, context) {
  const item = findItemByTitle_(form, record.title) || form.addCheckboxItem();
  item.setTitle(record.title);
  item.setHelpText(record.helpText || '');
  item.setChoiceValues(parseChoiceValues_(record.choices));
  item.setRequired(Boolean(record.required));
  context.log('Checkbox item updated.', { title: record.title });
}

function upsertParagraphItem_(form, record) {
  const item = findItemByTitle_(form, record.title) || form.addParagraphTextItem();
  item.setTitle(record.title);
  item.setHelpText(record.helpText || '');
  item.setRequired(Boolean(record.required));
}

function upsertTextItem_(form, record) {
  const item = findItemByTitle_(form, record.title) || form.addTextItem();
  item.setTitle(record.title);
  item.setHelpText(record.helpText || '');
  item.setRequired(Boolean(record.required));
}

function findItemByTitle_(form, title) {
  const items = form.getItems();
  for (var i = 0; i < items.length; i++) {
    if (items[i].getTitle() === title) {
      return items[i];
    }
  }
  return null;
}

function parseChoiceValues_(rawChoices) {
  if (!rawChoices) {
    return [];
  }
  const values = String(rawChoices)
    .split('\n')
    .map(function (choice) { return choice.trim(); })
    .filter(Boolean);
  return values;
}

/**
 * Sends a failure notification email with detailed logs and variable snapshots.
 *
 * @param {Error} error
 * @param {Object} context
 * @param {Object} config
 */
function notifyFailure_(error, context, config) {
  var recipients = [];
  if (config && config.recipients && config.recipients.length) {
    recipients = config.recipients;
  } else {
    recipients = (PropertiesService.getScriptProperties().getProperty('ALERT_RECIPIENTS') || '')
      .split(',')
      .map(function (email) { return email.trim(); })
      .filter(Boolean);
  }

  if (!recipients.length) {
    Logger.log('No alert recipients configured. Failure notification skipped.');
    return;
  }

  const snapshot = context.snapshot();
  const timezone = Session.getScriptTimeZone() || 'GMT';
  const startTime = Utilities.formatDate(snapshot.startTime, timezone, 'yyyy-MM-dd HH:mm:ss');
  const endTime = Utilities.formatDate(snapshot.endTime, timezone, 'yyyy-MM-dd HH:mm:ss');
  const durationSeconds = Math.round((snapshot.endTime.getTime() - snapshot.startTime.getTime()) / 1000);

  const emailBody = [
    'Process Name: ' + snapshot.processName,
    'Start Time: ' + startTime + ' (' + timezone + ')',
    'End Time: ' + endTime + ' (' + timezone + ')',
    'Duration (seconds): ' + durationSeconds,
    '',
    'Error Message:',
    (error && error.message) || '(no message)',
    '',
    'Stack Trace:',
    (error && error.stack) || '(stack trace unavailable)',
    '',
    'Captured Variables:',
    formatVariablesForEmail_(snapshot.variables),
    '',
    'Execution Log:',
    formatLogEntriesForEmail_(snapshot.logs),
    '',
    'Logger Output:',
    Logger.getLog() || '(no Logger entries)'
  ].join('\n');

  MailApp.sendEmail({
    to: recipients.join(','),
    subject: 'Google Form from Excel automation stopped unexpectedly',
    body: emailBody
  });
}

function formatVariablesForEmail_(variables) {
  const keys = Object.keys(variables || {});
  if (!keys.length) {
    return '(no variables captured)';
  }
  return keys.map(function (key) {
    return key + ': ' + safeStringify_(variables[key]);
  }).join('\n');
}

function formatLogEntriesForEmail_(logs) {
  if (!logs || !logs.length) {
    return '(no execution log entries)';
  }
  const timezone = Session.getScriptTimeZone() || 'GMT';
  return logs.map(function (entry) {
    const timestamp = Utilities.formatDate(entry.time, timezone, 'yyyy-MM-dd HH:mm:ss');
    const details = entry.details ? '\n  ' + safeStringify_(entry.details) : '';
    return '[' + timestamp + '] ' + entry.message + details;
  }).join('\n');
}

function safeStringify_(value, depth) {
  const maxDepth = 4;
  const maxArrayLength = 20;
  const currentDepth = depth || 0;

  if (value === null) {
    return 'null';
  }
  if (value === undefined) {
    return 'undefined';
  }
  if (typeof value === 'string') {
    return value;
  }
  if (typeof value === 'number' || typeof value === 'boolean') {
    return String(value);
  }
  if (value instanceof Date) {
    return value.toISOString();
  }
  if (Array.isArray(value)) {
    if (currentDepth >= maxDepth) {
      return 'Array(' + value.length + ')';
    }
    const items = value.slice(0, maxArrayLength).map(function (item) {
      return safeStringify_(item, currentDepth + 1);
    });
    const suffix = value.length > maxArrayLength ? ', ...' : '';
    return '[' + items.join(', ') + suffix + ']';
  }
  if (typeof value === 'object') {
    if (currentDepth >= maxDepth) {
      return 'Object(' + Object.keys(value).join(', ') + ')';
    }
    const keys = Object.keys(value);
    if (!keys.length) {
      return '{}';
    }
    const entries = keys.slice(0, maxArrayLength).map(function (key) {
      return key + ': ' + safeStringify_(value[key], currentDepth + 1);
    });
    if (keys.length > maxArrayLength) {
      entries.push('...');
    }
    return '{' + entries.join(', ') + '}';
  }
  return String(value);
}
