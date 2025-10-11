---
id: GUIDE-GWS-AND-GEMINI-USAGE-GUIDE-ENGLISH
title: GWS/Gemini Usage Guide (English Edition)
issuer: Trường Đại học Việt Nhật
category: Guide
issue_date: null
status: active
languages: [en]
source_pdf: ""
replaces: []
replaced_by: []
revision_history: []
tags: [guide]
---
# GWS/Gemini Usage Guide (English Edition)

This book is a handbook for faculty and staff members working at the university to utilize Google Workspace (hereafter GWS), the Gemini family of generative AI services, and related technologies such as Apps Script, Retrieval-Augmented Generation (RAG), and Multi-Channel Processing (MCP) in a systematic way. By following the chapters from basic file sharing to advanced automation, readers can gradually understand environment setup, daily use, and operations.

---

## Introduction

This chapter lists the main services and functions covered in the manual so readers can use it as a roadmap. Each topic is explained in detail in later chapters.

The manual highlights the following use cases and explains concrete procedures and precautions in the relevant chapters.

1. **Automated meeting minutes for hybrid meetings:** Record meetings in Google Meet, store the video in Drive, generate transcripts and summaries with Gemini, organize action items with Apps Script, and share the results on a shared drive.
2. **Real-time collaboration between instructional materials and student work:** Distribute exercises with Google Slides, let students write in the same deck simultaneously, summarize key takeaways with Gemini after submission, and visualize comprehension in Google Sheets.
3. **Building a knowledge base for research projects:** Organize materials in shared drives and Google Sites, load them into NotebookLM to generate literature comparisons and FAQs, and combine RAG to deliver answers that cite the latest resources.
4. **Digital assistant for day-to-day operations:** Use Gemini CLI to automate PC and printer setup or troubleshooting, download and install additional software, edit files stored on the device, and identify unnecessary files to free up storage.

### Google Workspace (Explained in Chapter 1)
- Google Groups: Centralized communication as a mailing list and message board.
- Shared Drives: Organization-owned storage; clarifies the differences from My Drive and explains access control.
- Google Docs: Real-time collaborative editing, templates, and shared comments.
- Google Sheets: Data sharing and analysis, pivot tables, and permission control.
- Google Slides: Collaborative creation of class and meeting materials and template management.
- Google Forms: Collecting applications and surveys with automatic aggregation.
- Google Calendar: Shared scheduling and resource management.
- Google Meet: Online meetings, recordings, and live captions.
- Google Sites: Publishing manuals and portals with access control.

### Generative AI (Explained in Chapter 2)
- Gemini (Web): Browser-based conversational AI for drafting, summarizing, and translation.
- Google Notebook (NotebookLM): Load materials to generate summaries and Q&A within a notebook interface.
- Google AI Studio: A development environment to prototype Gemini APIs, design prompts, and manage samples.
- Gemini CLI: A command-line interface for batch jobs and script-based workflows using the Gemini API.

### GAS and Related Technologies (Explained in Chapter 3)
- Google Apps Script (GAS): JavaScript-based automation for GWS with version control via clasp.
- RAG (Retrieval-Augmented Generation): A method that combines internal search with generative output.
- MCP (Multi-Channel Processing): Workflows that integrate text, audio, and images.

## Chapter 1: Leveraging Google Workspace

This chapter explains how to improve efficiency and collaboration using standard GWS features without AI. Because all services run in the cloud, users can access up-to-date information regardless of location or device.

### 1.1 Organizational Communication with Google Groups
- **Overview:** Google Groups functions as a mailing list, message board, and collaborative inbox, centralizing communication for departments, committees, and project teams. Threads are accessible on the web in addition to email.
- **Integration with Other Services:** Assign the group address to Google Calendar invitations and shared drives so that schedules, materials, and tasks stay synchronized with membership changes.
- **Member Management:** Administrators can add or remove members by role and process changes in bulk for transfers and enrollment. Dynamic groups automate maintenance based on organizational units, and access to shared drives and calendars is updated automatically in sync with membership operations.
- **Collaborative Inbox:** Enable the collaborative inbox to assign tickets and track their status—the same workflow adopted by customer support and IT help desks in the private sector—so the team can distribute inquiries from students and staff.
- **Use Cases:** Course announcements, school-wide notifications, committee minutes, research collaboration, student project Q&A, and more.
- **Archive:** Messages accumulate in a searchable archive that supports transitions, audits, and knowledge sharing. Even if emails are deleted from personal inboxes, the group maintains the history.
- **Moderation:** Configure approval workflows, spam filters, and keyword-based holds to control information quality. This is particularly helpful when using Groups as a student inquiry board.
- **Notification Preferences:** Members can choose how frequently they receive mail (all messages, digest, or none) to avoid notification overload while keeping essential updates.
- **Labels and Categories:** Apply labels or categorize threads to improve searchability and build an FAQ-style knowledge hub.
- **Reporting:** Use the Google Workspace admin console to review access logs and audit reports, monitoring for unauthorized access or potential data leaks.
- **Security:** Grant finely controlled permissions to external members (view-only, no posting, etc.), and enforce second-stage approvals or expiry dates for sensitive information.
- **Reference:** [Manage Google Groups (Google Groups Help)](https://support.google.com/groups?hl=ja)

### 1.2 File Sharing and Shared Drive Operations
- **Shared Ownership vs. My Drive:** My Drive is owned by individuals, so documents may be lost when people leave. Shared drives are owned by the organization, ensuring smoother handovers.
- **Real-time Co-editing:** Multiple users can edit simultaneously from a browser or mobile device without conflicts, and version history allows restores.
- **Access Logs and Audit Trails:** Track viewing, editing, and permission changes for internal control and data-leak prevention. Integrate with SIEM tools for automated monitoring.
- **Standard Folder Structure:** Establish a uniform hierarchy, such as “00_Template,” “01_In Progress,” “10_Published,” and “99_Archive,” so cross-departmental teams can locate materials quickly.
- **Metadata and Naming Convention:** Standardize filenames (e.g., “YYYYMMDD_Department_DocumentType_Version”) and record author/edit dates in the document for easier search and auditing.
- **Permission Templates and Auto-assignment:** Create permission sets (view-only, comment, edit, manager) and assign them by Google Group to streamline access management.
- **Lifecycle Management:** Represent statuses (in progress → published → archived) with folders and review archival folders regularly to optimize storage.
- **External Collaboration and Time-limited Access:** Grant guest access to external collaborators with expiry dates and download restrictions; revoke access automatically and keep logs when projects end.
- **Data Retention and Recovery:** Shared drives support restores within 30 days; combine with Vault or backup tools for long-term retention and eDiscovery.
- **Governance and Training:** Document sharing policies, security rules, training, FAQs, and checklists to ensure adoption.
- **Reference:** [Shared drives overview (Google Workspace Admin Help)](https://support.google.com/a/answer/7212025?hl=ja), [Manage shared drives (Google Workspace Admin Help)](https://support.google.com/a/answer/7281227?hl=ja)

### 1.3 Document Creation with Google Docs
- **Collaborative Editing:** Multiple editors can work simultaneously without conflicts while comments and suggestion mode visualize decision-making.
- **Templates:** Store syllabi, meeting minutes, and forms in shared drives for quick reuse.
- **Tabbed Layouts:** Unique building blocks like tabbed pages and tables help separate lecture sessions, agenda items, or departments.
- **Translation Tool:** “Tools > Translate document” creates a translated copy for multilingual materials or international meetings.
- **Version History and Comparison:** Track revisions chronologically and compare or restore specific versions, supporting approval workflows and audit trails.
- **Comments and Task Assignment:** @mention colleagues in comments to notify them via email and automatically assign tasks for proofreading and approval.
- **Voice Typing and Accessibility:** Voice input and screen-reader support speed up lecture transcription and accessible material development.
- **Smart Chips:** Insert files, calendar events, or user info from Drive as smart chips for one-click access.
- **Approval Workflow:** Use “File > Share & Approve” to set approvers, deadlines, and notes. Approvers can accept or request changes with a single click, and the system records decision history while sending email notifications—including overdue reminders.
- **Automation Integrations:** Use Apps Script or add-ons to insert reusable content blocks or auto-generate documents from form responses.
- **Reference:** [Get started with Google Docs (Google Docs Help)](https://support.google.com/docs?hl=ja#topic=1382883), [Use building blocks like paginated tables (Google Docs Help)](https://support.google.com/docs/answer/12112505?hl=ja)

### 1.4 Data Sharing with Google Sheets
- **Real-time Data:** Keep attendance, research budgets, and student rosters up to date in one sheet. Version history tracks changes.
- **Collaborative Editing:** Teaching staff, advisors, and administrators can edit simultaneously, with comments and suggestions capturing discussion history.
- **Analysis Tools:** Filter views, pivot tables, Explore, and charts visualize data intuitively.
- **Conditional Formatting:** Automatically highlight values exceeding thresholds to spot anomalies quickly.
- **Data Validation:** Use dropdowns and regex to control inputs and reduce form errors and duplicates.
- **Integrations and Automation:** Connect with Forms, Apps Script, and Looker Studio to automate aggregation, notifications, and reporting.
- **Import Functions:** Pull data from CSV, other sheets, and APIs (`IMPORTRANGE`, `IMPORTDATA`) to synchronize with external systems.
- **Shared Drive Integration:** Store Sheets in shared drives so access is managed by group membership; permissions update automatically when people leave.
- **Scenario Applications:** Budget simulations, career guidance, course surveys, timetable adjustments, and more.
- **Audit and Protection:** Protect ranges, lock cells, and enable change notifications to monitor critical data.
- **Reference:** [Get started with Google Sheets (Google Sheets Help)](https://support.google.com/sheets?hl=ja#topic=2811806)

### 1.5 Class and Meeting Management with Google Slides
- **Co-editing:** Students can edit different slides in the same deck simultaneously while instructors offer real-time feedback.
- **Templates and Masters:** Apply department-wide templates via the master deck to standardize brand colors, logos, and fonts; updates propagate automatically.
- **Distribution and Publishing:** Share the latest version through web publishing, PDF export, or viewer links for students and external partners.
- **Speaker Notes:** Add detailed explanations or references to presenter notes so slides double as self-learning materials or meeting records.
- **Comments and Q&A:** Gather questions and conduct Q&A directly on slides.
- **Media Insertion:** Embed videos, audio, shapes, and smart chips to present lab experiments or case studies interactively.
- **Version History:** Save and compare past versions to capture annual course updates and presentation improvements.
- **Access Control:** Set granular permissions (viewer/commenter/editor) and restrict to view-only during evaluation periods.
- **Presentation Support:** Use presenter view, laser pointer, and live captions to support online and hybrid classes.
- **Automation:** Use Apps Script or add-ons to generate slides, translate content, or insert diagrams automatically, reducing time spent on routine decks.
- **Reference:** [Get started with Google Slides (Google Slides Help)](https://support.google.com/slides?hl=ja#topic=9054607)

### 1.6 Data Collection with Google Forms
- **Instant Aggregation:** Responses populate connected Sheets in real time, enabling progress tracking and automated notifications.
- **Reservations and Applications:** Use for workshop registration, equipment booking, course evaluations, advising appointments, and event signups.
- **Branching:** Ask only relevant questions by branching based on responses.
- **Validation and Guidance:** Apply input limits, helper text, and progress bars to reduce errors and improve completion rates.
- **File Uploads:** Collect assignments or supporting documents directly in Drive.
- **Notifications and Approvals:** Combine response notifications with Apps Script and Gmail templates to build approval workflows. Add-ons such as Form Approvals let you notify supervisors automatically when a remote-work request is submitted and allow them to approve or reject it directly from the email.
- **Multilingual Support:** Use sections or multiple forms to support Japanese-English displays for international students.
- **Custom Themes:** Apply school colors and logos to maintain brand consistency and build trust.
- **Publication Settings:** Limit to the campus, anyone with the link, or public Q&A as needed.
- **Analytics Integration:** Build dashboards in Looker Studio or Apps Script to share insights with management immediately.
- **Reference:** [Get started with Google Forms (Google Forms Help)](https://support.google.com/docs/topic/6063584?hl=ja)

### 1.7 Scheduling with Google Calendar
- **Shared Events:** Manage meetings, classes, and deadlines so everyone sees the latest schedule in real time.
- **Appointment Slots:** Publish office hours, consultation slots, or equipment bookings so requesters can pick available times.
- **Invitations and Attachments:** Attach Drive files and related links to invitations to prompt preparation.
- **Reminders:** Combine email, pop-up, and mobile notifications to prevent missed events.
- **Access Control:** Set roles (view-only, see event details, edit, manage) to protect privacy.
- **Time Zone Support:** Display multiple time zones for international meetings with branch campuses or exchange students.
- **Attendance Tracking:** Monitor RSVPs within Calendar and automatically send follow-up emails to absentees.
- **Resource Booking:** Register classrooms, meeting rooms, and equipment as resources to visualize availability. Open the event editor, click “More options,” search for the desired room under “Add conferencing or location,” and select it to view available time slots. Conflicts trigger a warning. For recurring use, set the event to repeat and add usage notes or layout requests in the description for stakeholders.
- **Calendar Overlay:** Overlay personal, departmental, and university calendars to detect conflicts by color.
- **History and Logs:** Review who modified events and when.
- **Reference:** [Google Calendar basics (Google Calendar Help)](https://support.google.com/calendar?hl=ja#topic=10509771)

### 1.8 Online Meetings with Google Meet
- **Meeting Creation:** Generate meeting links with one click via Calendar and share automatically with invitees.
- **Parity with Zoom:** Most features used in Zoom—screen sharing, recording, breakout rooms, polls, and more—are available in Google Meet. Because you already have a GWS university account, no new account creation or payment is required.
- **Recording and Sharing:** Record sessions automatically to Drive for absent participants or minute-taking.
- **Captions and Translation:** Provide live captions and multilingual translation to enhance accessibility and international collaboration.
- **Breakout Rooms:** Create breakout rooms for small-group discussions in classes or workshops.
- **Polls and Q&A:** Conduct polls and Q&A during meetings to gather feedback in real time.
- **Interactive Whiteboard:** Share Google Slides as a collaborative whiteboard for joint brainstorming.
- **Security:** Use waiting rooms, participant limits, noise cancellation, and background blur to improve security and user experience.
- **Device Integration:** Combine Meet hardware and mobile devices for hybrid classrooms and conference rooms.
- **Live Streaming:** Broadcast to up to 100,000 viewers with live-streaming mode and keep recorded archives.
- **Automation:** Use Apps Script or the CLI to retrieve attendance logs or generate meeting-minute templates automatically.
- **Reference:** [Google Meet overview (Google Meet Help)](https://support.google.com/meet?hl=ja)

### 1.9 Google Sites and Portal Operations
- **Campus Portals:** Centralize course materials, application procedures, FAQs, and guidelines to streamline user navigation.
- **Access Control:** Configure internal-only, department-only, or public access depending on data sensitivity.
- **Templates:** Apply organization-wide templates to standardize branding and build pages quickly.
- **Drag-and-drop Editing:** Easily adjust layouts and embed images and content with intuitive editing tools.
- **Drive Integration:** Embed Docs, Sheets, Slides, and Forms to display the latest information automatically.
- **Navigation:** Use page hierarchies, tables of contents, and search to help users find what they need quickly.
- **Responsive Design:** Automatically adjusts to PCs, tablets, and smartphones.
- **Reference:** [Get started with Google Sites (Google Sites Help)](https://support.google.com/sites?hl=ja#topic=7184583)

---

## Chapter 2: Leveraging Generative AI (Gemini and More)

This chapter explains how to use Google’s Gemini services to support writing, analysis, and application development. Each service is introduced with an overview, onboarding steps, use cases, and prompt examples.

For the Gemini offering provided within VJU’s Google Workspace environment, contractual terms guarantee that user inputs are **not** reused as Google’s training data. As long as you access Gemini with your campus account, prompts are processed in the organization’s dedicated environment and are not fed back into model training.

### 2.1 Principles for Using Generative AI
1. **Clarify Goals and Constraints:** Include goals, target audience, output format, and prohibitions in the prompt.
2. **Stage Your Requests:** Break large tasks into smaller steps and ask the AI sequentially to increase accuracy.
3. **Verification Process:** Always review outputs, verify citations and numbers, and ensure compliance with laws and policies.
4. **Security:** Mask or summarize personal data and unpublished research before sharing with AI.
5. **Data Classification:** Define the level of sensitivity and what kinds of data are allowed in prompts ahead of time.
6. **Prompt Management:** Record both successful and failed prompts to build organizational knowledge and iterate.
7. **Human-in-the-loop:** Keep humans in charge of critical decisions and use AI as an assistant.
8. **Pilot Projects:** Run small PoCs, validate success metrics and risks, then scale campus-wide.
9. **Rights and Ethics:** Address copyright, research ethics, and bias. Establish and communicate usage policies.
10. **Continuous Learning:** Analyze logs and feedback, and update prompts and training materials regularly.

Documenting prompts and reference materials in Markdown—a human-readable and AI-friendly text format—simplifies version control, reuse, and integration with NotebookLM or RAG workflows.

- **Reference:** [Best practices for safe generative AI (Google AI Docs)](https://ai.google.dev/docs/safety?hl=ja)

### 2.2 Gemini (Web)
**Overview:** A browser-based conversational AI for text generation, translation, summarization, ideation, and more.

**Onboarding Steps:**
1. Access Gemini with your Google account (https://gemini.google.com/).
2. Review the terms of use and data usage policy.
3. Request Gemini for Workspace licenses from the administrator if necessary.

**Use Cases:**
- Design lecture plans, syllabus outlines, and learning objectives.
- Adjust tone for student emails, parent communications, and campus announcements.
- Summarize meeting minutes, extract action items, and draft follow-up emails.
- Upload research proposals or grant applications to receive constructive feedback on structure and methodology.
- Draft internal university proposals and align them with previously accepted examples.
- Check application packets or administrative forms for careless mistakes (typos, missing entries, or formatting issues) and obtain correction suggestions.
- Create case studies, discussion questions, and exercises for classes.
- Generate reference lists and related keywords.
- Translate and adapt materials for international students.
- Connect with Gmail, Google Calendar, and Google Drive to summarize inboxes, draft replies, organize shared-drive documents, and coordinate schedules in one flow.
- Draft FAQ responses and chatbot templates.
- Build and share Gems (public prompts) that preload admissions guidelines or scholarship information, so prospective students get policy-aligned answers while inquiries outside the handbook trigger guidance to contact the appropriate office.
- Draft student support responses and email templates.
- Summarize administrative documents and compare policy revisions.

**Prompt Examples:**
- **Reference:** [Gemini (Google Help Center)](https://support.google.com/gemini?hl=ja)
```
Goal: Create a 90-minute orientation script for new university students.
Instructions:
- Structure with introduction, campus tour, enrollment system explanation, and Q&A.
- List the facilitator, required materials, and expected questions for each part.
- Include an icebreaker activity at the beginning to ease student anxiety.
```

```
Goal: Develop a case study for a research ethics workshop.
Instructions:
- Provide a clinical research scenario for STEM graduate students.
- Include background, issues, discussion points, and references.
- Prepare three discussion questions for participants.
```

```
Goal: Obtain constructive feedback on the attached research proposal (PDF).
Instructions:
- Review the research objectives, methodology, and timeline in the file and list strengths and improvement points.
- Evaluate briefly whether the objective is academically novel compared with existing studies.
- Point out missing data, validation procedures, or ethical considerations.
- Conclude with the top three items to fix in the next revision.
```

```
Goal: Identify careless mistakes in the attached application documents.
Instructions:
- List typos, blank fields (dates, names, etc.), and deviations from the required format.
- Provide a correction suggestion and rationale for each item, with priority labeled High/Medium/Low.
- If a mandatory field is blank, suggest an example of the expected content.
```

```
Goal: Draft a new internal proposal consistent with past approved examples.
Instructions:
- Read the PDFs in the attached “Reference Proposals” folder and summarize the common structure and tone.
- Create a draft that follows the order: overview, objectives, activity plan, evaluation metrics, and budget for this year’s theme “Curriculum Improvement through Regional-Industry Collaboration.”
- Note which elements were adapted from past materials and list any additional information still required.
```

```
Goal: Coordinate actions across Gmail, Calendar, and Drive.
Instructions:
- Summarize the past seven days of Gmail threads labeled “Research Grant,” highlighting messages that still require responses.
- Review the “/Grants/2025” folder in Google Drive, extract key points from the three most recently updated documents, and list outstanding tasks.
- Check Google Calendar and suggest three open time slots for next week, then draft a response sentence that proposes these slots.
```

### 2.3 Google Notebook (NotebookLM)
**Overview:** A notebook-style AI that ingests documents (Docs, PDFs, Slides, etc.), supports up to 50 resources, and enables high-accuracy document understanding with conversational knowledge management.

**Use Cases:**
- Generate quiz questions from an entire syllabus for quizzes and review sheets.
- Compare research papers by summarizing objectives, methods, results, and challenges.
- Categorize student reports by rubric and recommend improvements.
- Extract discussion points and decisions from committee minutes and policy documents.
- Summarize survey reports with key findings and citations to prepare presentations.
- Register reference PDFs and extract related keywords and emerging themes.
- Produce vocabulary lists, cloze exercises, and conversation scenarios from language-learning materials.
- Analyze university regulations to map the scope of revisions and differences.
- Cluster open-ended survey comments and draft improvement ideas.
- Consolidate project documents to summarize progress, risks, and next actions.
- **Reference:** [NotebookLM overview (NotebookLM Help)](https://support.google.com/notebooklm?hl=ja)

**Prompt Examples:**
```
Goal: Summarize “2024 Curriculum Reform Proposal.pdf” and extract discussion points.
Instructions:
- Summarize key points for each chapter in 200 characters or less.
- List three potential impacts on students and three preparation items for faculty.
```

```
Goal: Create review questions for Week 8 of the course.
Instructions:
- Refer to the registered slides and handouts to generate three multiple-choice and two short-answer questions.
- Provide the correct answer and explanation for each question.
```

### 2.4 Google AI Studio
**Overview:** A browser-based environment for experimenting with the Gemini API. It supports prompt design, few-shot sample management, API key issuance, and validation of workflows that handle diverse files—PDF, audio, images—for text extraction and summarization accuracy.

**Onboarding Steps:**
1. Access Google AI Studio and create a new project.
2. Select a model (e.g., Gemini 1.5 Pro) and output format (text or JSON).
3. Configure system instructions and input/output samples to fine-tune results.
4. Generate an API key and integrate it with Apps Script or external applications.
- **Reference:** [Google AI Studio](https://ai.google.dev/aistudio?hl=ja)

**Ideas for Use:**
- Prototype FAQ chatbots and inquiry assistants quickly.
- Pilot research-data summarization before integrating with Apps Script.
- Run prompt comparison experiments to test instructions and temperature settings.
- Define JSON response templates for system integrations.
- Share projects with teammates to reproduce tests under the same configuration.
- Use it as a training sandbox for student assistants learning prompt design.
- Issue API keys for batch processing and combine with Apps Script or the CLI for testing.
- Create evaluation sheets to compare model versions when switching releases.
- Review logs and errors to identify governance risks or constraints.
- Experiment with multilingual prompts and multimodal inputs for future expansion.
- Upload PDF, audio, or image files to convert them into text or summaries and automate groundwork for materials or minutes.

### 2.5 Gemini CLI
**Overview:** A command-line tool for interacting with the Gemini API. It excels at batch processing and scripted workflows, while also leveraging local file operations and device settings.

**Onboarding Steps:**
1. Install the LTS version of Node.js. Download the installer labeled “LTS” from the official site (https://nodejs.org/ja) and follow the on-screen instructions. After installation, run `node -v` and `npm -v` in the terminal to confirm it is ready.
2. Install the CLI via `npm install -g @google/gemini-cli`.
3. Authenticate with `gemini login`.
4. Use commands such as `gemini prompt` and `gemini models list`.

**Use Cases:**
- Schedule regular translation or summarization jobs with cron and save results to Drive.
- Read and write local files to automate organization, format conversion, and backups.
- Script software downloads and installations to set up most applications automatically.
- Analyze CSV or JSON data and generate dashboards or summary reports.
- Version-control custom prompts in a repository for reuse.
- Automate research data preprocessing (column descriptions, statistical summaries, anomaly hints).
- Check documents, spreadsheets, and manuals for careless mistakes before submission and extract fix suggestions.
- Process collections of abstracts to extract keywords or classifications.
- Template exam or exercise questions and generate multiple variants.
- Run overnight batch jobs with workflow tools or shell scripts.
- Send CLI output to Slack or Chat webhooks for real-time team updates.
- Troubleshoot PC-related issues—printer setup, driver updates, network connectivity—through interactive guidance.
- Prepare mock datasets and prompt evaluation benchmarks.
- Combine with Apps Script or external APIs to build serverless AI backends.
- **Reference:** [Gemini API Quickstart (CLI) (Google AI Docs)](https://ai.google.dev/gemini-api/docs/quickstart?hl=ja#cli)

**Prompt Examples:**
```
cat syllabus.txt | gemini prompt \
  --model gemini-pro \
  --system "You are a teaching assistant who summarizes course outlines." \
  --prompt "From the syllabus above, extract the learning objectives, assessment methods, and assignment schedule in a table."
```

```
cat application_form.md | gemini prompt \
  --model gemini-pro \
  --system "You work in university administration and review submitted forms." \
  --prompt "List typos, blank required fields, and format violations in the document above. Provide a correction proposal and a High/Medium/Low priority for each item."
```

```
cat survey.csv | gemini prompt \
  --model gemini-pro \
  --prompt "Read the CSV data and list the top three questions with the lowest satisfaction along with improvement ideas."
```

### 2.6 Practical Prompt Design
- **Role Definition:** Specify roles such as “You are a subject matter expert…” to inject the desired perspective.
- **Input Preprocessing:** Organize source documents (Markdown, tables) for reliable context.
- **Constraint Settings:** Define tone, format, length, language, and references explicitly.
- **Iterative Refinement:** Adjust prompts based on outputs and document successful patterns.
- **Verification:** Compare AI output with source materials and gather peer review feedback.
- **Prompt Libraries:** Store prompts in shared drives or repositories for discoverability and reuse.
- **Ethical Considerations:** Note restrictions (e.g., no personal data) directly in the prompt.
- **Fallback Plans:** Design alternative prompts or manual procedures in case of system issues.
- **Testing:** Establish evaluation metrics (accuracy, tone, coverage) and sample datasets.
- **Accessibility:** Ensure generated content meets accessibility and inclusivity guidelines.

---

## Chapter 3: Automation with GAS, RAG, and MCP

This chapter describes how to combine Apps Script, Gemini APIs, and external services to build automation workflows—from lightweight scripting to full-scale systems.

### 3.1 Overview of Apps Script, clasp, and Deployment
- **Apps Script Features:** Cloud-based editor, trigger scheduling, and deep GWS integration.
- **clasp Workflow:** Develop locally with version control and push changes to Apps Script projects.
- **Deployment Practices:** Maintain development, staging, and production deployments. Set policies to prevent direct edits in production.
- **Testing Automation:** Integrate CI/CD tools (GitHub Actions, Cloud Build) to lint code, run tests, and deploy automatically.
- **Error Handling:** Implement logging, notifications, and retries. Log detailed errors in Sheets or BigQuery.
- **Security:** Apply least privilege, protect secrets (vaults, Secret Manager), and audit triggers regularly.
- **Reference:** [clasp GitHub Repository](https://github.com/google/clasp)

### 3.2 Gemini API Integration with Apps Script
- **Prerequisites:** Create a Google Cloud project, enable the Gemini API, and manage API keys securely.
- **HTTP Requests:** Use `UrlFetchApp.fetch` to send requests; handle JSON parsing and errors.
- **Prompt Templates:** Store prompts with version numbers and environment variables to ensure consistent output.
- **Caching:** Leverage `CacheService` to reuse responses and reduce costs.
- **Logging:** Output prompt and response metadata to Sheets/BigQuery for traceability.
- **User Interfaces:** Build Apps Script web apps or chat interfaces for faculty and students.
- **Error Handling:** Define fallback answers or manual escalation steps for unexpected output.
- **Compliance:** Mask personal data, log consent, and enforce organizational policies.
- **Reference:** [Gemini API overview (Google AI Docs)](https://ai.google.dev/gemini-api/docs?hl=ja)

### 3.3 Retrieval-Augmented Generation (RAG)
- **Pipeline:** Define preprocessing, embedding, vector storage, retrieval, and generation.
- **Data Sources:** Use Docs, Sheets, Sites, and PDF repositories. Convert and clean data with Apps Script or Google Cloud tools.
- **Embedding Storage:** Choose Vertex AI Matching Engine, Firebase, or third-party vector databases.
- **Prompt Composition:** Inject retrieved passages into prompts with citations to increase reliability.
- **Evaluation:** Measure answer accuracy, citation correctness, latency, and user satisfaction.
- **Maintenance:** Update indexes regularly, track document versions, and remove outdated content.
- **Security:** Restrict data ingestion to approved sources, manage access keys, and log retrieval activity.
- **Reference:** [RAG architecture (Google Cloud)](https://cloud.google.com/architecture/rag-overview?hl=ja)

### 3.4 Multi-Channel Processing (MCP)
- **Concept:** Combine text, audio, images, and structured data for advanced workflows.
- **Implementation:** Integrate Gemini API with speech-to-text, translation, or vision services.
- **Use Cases:**
  - Convert recorded lectures into transcripts, highlight key points, and auto-generate follow-up tasks.
  - Sync photo diaries from field research and auto-generate localized reports.
  - Analyze multimedia teaching materials and output summaries, quizzes, and supplementary content.
- **Reference:** [Multimodal generative AI overview (Google Cloud Vertex AI Docs)](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/overview?hl=ja)

### 3.5 Project Design and Governance
- **Requirements Definition:** Document goals, stakeholders, data flows, security requirements, and SLAs.
- **Scope Management:** Separate MVP from phased enhancements and set priorities with a roadmap.
- **Team Structure:** Clarify roles for developers, IT, user departments, and auditors.
- **Test Strategy:** Prepare test cases for unit, integration, and UAT scenarios, including exceptions.
- **Change Management:** Track specification and prompt changes via tickets with review and approval flows.
- **Operations Monitoring:** Define logging, error alerts, health checks, and escalation procedures.
- **Security:** Manage Gemini API keys and OAuth credentials carefully, enforce least privilege, and apply data masking.
- **Compliance:** Periodically review personal data protection, research ethics, and record retention policies.
- **Training and Support:** Provide manuals, FAQs, help desks, and training sessions to drive adoption.
- **Continuous Improvement:** Review KPIs and feedback, update improvement plans, and schedule releases.
- **Reference:** [Google Workspace Security Center](https://workspace.google.com/intl/ja/security/)

### 3.6 Implementation Checklist
1. **Project Management:** Establish version control (Git), documentation, and code review practices.
2. **Requirements Traceability:** Track change history and impact analysis.
3. **Security:** Protect credentials, minimize permissions, encrypt data, and audit logs.
4. **Observability:** Collect logs, metrics, and alerts to detect anomalies and define response procedures.
5. **Backup:** Back up source code, configurations, and data regularly and verify restore procedures.
6. **SLA/SLO:** Set targets for uptime, response times, and support coverage; monitor actual performance.
7. **Evaluation:** Measure time saved, error reduction, user satisfaction, and cost savings.
8. **Training and Communication:** Update manuals, FAQs, and training materials; hold regular briefings.
9. **Risk Management:** Plan fail-safe designs, exception handling, and manual override steps.
10. **Continuous Improvement:** Use feedback and log analysis to refresh roadmaps and release plans.
- **Reference:** [Google Workspace Learning Center](https://support.google.com/a/users?hl=ja)

---

## Appendix A: Deployment and Operations Guidelines

1. **Account Management**
   - Enforce two-factor authentication for faculty and staff accounts.
   - Audit shared drive permissions regularly.
2. **Training Program**
   - Deliver three levels of training: basic GWS usage, generative AI applications, and advanced GAS/RAG integration.
   - Provide on-demand materials (videos, handbooks) via Sites.
3. **Operating Rules**
   - Establish generative AI usage policies covering restricted data, prompt examples, and review procedures.
   - Define review and approval workflows before using Apps Script or APIs in production.
4. **Evaluation and Improvement**
   - Review KPIs (work hours, error counts, satisfaction) quarterly.
   - Share success stories in briefings or newsletters to encourage adoption across campus.

---

## Appendix B: Reference Resources

- [Google Workspace Admin Help](https://support.google.com/a?hl=ja)
- [Gemini for Workspace](https://workspace.google.com/products/gemini/?hl=ja)
- [Google AI Studio Documentation](https://ai.google.dev/aistudio?hl=ja)
- [Apps Script Sample Gallery (Google Developers)](https://developers.google.com/apps-script/samples?hl=ja)
- University knowledge base (usage guidelines, prompt collections, FAQs)

Apply the contents of this manual to build a solid foundation with standard Google Workspace functions, then gradually layer generative AI and automation techniques. Reflect each chapter in training sessions and pilot projects, and keep improving through continuous feedback to balance operational efficiency with the quality of education and research.
