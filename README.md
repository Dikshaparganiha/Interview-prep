# Senior Backend / Platform Interview Question Database

Prepared for Diksha Parganiha on 2026-10-19 from the supplied profile and public sources. The primary deliverable is an individually searchable question bank, not a topic syllabus. Questions are practice formulations grounded in technical references and broad role expectations; they are not represented as verbatim, company-specific interview reports.

## Start Here

The primary deliverable is [interview-question-database.xlsx](interview-question-database.xlsx), with an autofilterable Question Bank, coverage counts, research sources, and a Top 200 Risk Drills sheet. The complete data is also in [question-database.csv](question-database.csv). Install [requirements.txt](requirements.txt), then run [generate_question_database.py](generate_question_database.py) to regenerate both.

The older [interview-prep.xlsx](interview-prep.xlsx) is the superseded topic-oriented version; use the question database linked above.

1. Filter by Category, Topic, Difficulty, or Importance Score and work directly from the Question column.
2. Use Expected Answer as a scoring checklist, not a script; practice follow-ups without looking.
3. Read [market-research.md](market-research.md) for evidence boundaries and the market signals that informed priority.
4. Use [execution-plan.md](execution-plan.md) to structure practice time; it supplements, not replaces, the question database.
5. Map behavioral and resume-based prompts to truthful examples. Do not invent experience or metrics.
6. Validate employer-specific expectations against each job posting and recruiter guidance.

## Coverage

The database contains 9,500 distinct question records: Go 1,500; DSA 1,450; Distributed Systems 1,000; System Design 1,000; Kafka 500; PostgreSQL 500; Redis 250; MongoDB 250; Kubernetes 500; AWS/Azure 500; Security 500; Behavioral 500; AI/LLM 550; Resume-Based 500. Every listed Go concept, DSA problem, and system-design scenario has 50 question formulations across beginner, intermediate, advanced, senior, Staff, Principal, debugging, failure, performance, architecture, tradeoff, and synthesis lenses. The 200 risk drills are a ranked practice set, not a statistically measured list of the 200 most frequent causes of interview failure.

## Candidate Fit Hypothesis

The profile is strongest for senior backend and platform roles that combine Go services, distributed systems, cloud security, event-driven architecture, data storage, Kubernetes, and production operations. A particularly credible differentiator is explaining how backend correctness and platform reliability meet in a real domain such as EV charging or cloud security. The next career-level gap to prove for Lead/Staff roles is not another technology name: it is documented scope across teams, strategy under ambiguity, adoption, delegation, influence, and measurable durable impact.

This is a hypothesis based on the supplied profile and relevant repository context, not a resume review. The workspace did not contain a resume/CV, so no claim here attributes a specific project, metric, role outcome, or accomplishment beyond what was supplied.

## Company Table: How to Read It

The CSV contains 100 distinct company targets. **Priority rank, role-match percentage, and difficulty are heuristic planning scores**, not measured hiring probabilities or compensation estimates. Interview pattern and round count are only stated where a company-published source was validated in this research pass. Most other fields say to verify the exact requisition because interview loops, language use, Kafka usage, AI emphasis, compensation, and even hiring organization vary by role, location, and date.

The table intentionally does not fabricate compensation. To estimate it responsibly, provide country/city, target level/title, currency, and whether total compensation should include bonus/equity. Use current job postings and location-specific compensation sources, not one global company range.

## Important Limits and Next Inputs

- **Resume-based prompts:** the 500 rows are profile-based interview probes, not analysis of unseen resume bullets. No resume was present, so verify every premise against actual experience before answering.
- **Compensation ranges and application ranking:** need target geography, work authorization/relocation constraints, preferred work model, and target level.
- **Company-specific process database:** the table is a 100-company discovery universe. Recruiter-confirmed round counts, language, AI-use policy, Go/Kafka evidence, and current compensation need current role-level validation.
- **Question saturation:** no finite database guarantees that no interviewer can ask a new question. These rows span major technical, operational, behavioral, and seniority lenses; expand from actual role descriptions, recruiter guidance, and mock feedback.
- **AI interviews:** survey data supports growing AI-tool use, but does not establish that AI coding interviews or agent-design rounds are universal. Ask each recruiter about permitted tools and assessment format.

## Evidence Discipline

Company hiring pages are the best evidence for that company's stated process; they do not guarantee every hiring team uses an identical loop. Surveys describe respondents, not interview questions. Engineering blogs and official documentation establish system concepts, not hiring frequency. Public interview reports are noisy and can be stale or location-specific. The Company and Frequency fields describe role-family fit and qualitative estimates, not verified counts of named-company occurrences. Questions are deduplicated practice formulations generated from topic-specific interview lenses; their count is not evidence of market prevalence.

## Update Cadence

Refresh company-role facts when applying, then add or revise question rows after each recruiter screen and mock interview. Record source URL, access date, role title, location, and confidence for any new company-specific claim.
