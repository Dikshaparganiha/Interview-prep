# Interview Preparation Execution Plan

**Time assumption:** 2-3 hours on each weekday and 6-8 hours on each weekend day, about 22-31 focused hours per week. These are capacity envelopes; protect recovery time and use quality of practice rather than hours alone as the success measure.

## Pareto Focus: Highest-Return 20%

1. Timed coding fundamentals in one interview language (Go), including explanation, edge cases, and tests.
2. System-design method and core backend primitives: APIs, databases, queues, caching, partitioning, consistency, failure handling.
3. Go concurrency, cancellation, races, profiling, and production debugging.
4. SQL/PostgreSQL transaction, index, and query-plan reasoning plus Kafka delivery/consumer-group semantics.
5. Senior-level project narratives: ownership, technical decisions, influence, failures, reliability, measurable outcomes.
6. Security and production operations: identity/authorization, tenant boundaries, SLOs, observability, incident response.

This selection is a role-fit judgment, not a measured universal 80/20 law. AI, deep consensus proofs, niche runtime internals, and extensive company trivia come after these unless a target job description elevates them.

## Weekly Operating Rhythm

| Day | Session design (2-3 hours) |
| --- | --- |
| Monday | 60-75 min timed coding; 45 min review; 30-45 min Go fundamentals or DS&A weak spot |
| Tuesday | 60 min system design; 45 min database/distributed-systems concept; 30 min verbal explanation |
| Wednesday | 60-75 min coding; 45 min Go concurrency/testing; 30 min behavioral story rehearsal |
| Thursday | 60 min system design; 45 min Kafka/cloud/security; 30 min failure-mode drill |
| Friday | 45 min coding redo; 45 min weekly error-log review; 30-60 min mock behavioral or rest if fatigued |
| Saturday | 90 min full coding mock; 90 min system-design mock; 60 min targeted study; 60-120 min hands-on project or review |
| Sunday | 60-90 min behavioral mock; 90 min design/coding redo; 60 min spaced recall; 60-120 min weekly planning or recovery |

Use a mistake log with four fields: problem, missed signal, root cause, next repetition date. Re-solve missed coding questions from a blank editor after 1 day, 1 week, and 3 weeks. For design, write a one-page design from memory, then compare against the rubric.

## 30-Day Plan: Rebuild the Interview Baseline

**Outcome:** Interview-ready fundamentals, one complete system-design method, six defensible behavior stories, and a clear gap list. At 22-31 hours/week this is approximately 90-125 focused hours.

| Week | Focus | Required outputs |
| --- | --- | --- |
| 1 | Baseline diagnostics; arrays/hash maps, strings, two pointers, stacks/queues; Go syntax/value semantics/interfaces | 2 timed coding mocks; baseline scorecard; 10 solved/reviewed problems; Go nil/interface/slice explanation |
| 2 | Trees, heaps, binary search, BFS/DFS, intervals; Go goroutines/channels/context/race detector | 12 additional problems; cancellable bounded worker pool; 1 concurrency mock; 3 STAR stories |
| 3 | PostgreSQL SQL/indexes/MVCC; Kafka partition/consumer/offset/retry; system design method | Explain 5 transaction/queue failure cases; design URL shortener and notification service; 4 more stories |
| 4 | Distributed systems, API security, observability, behavioral loop; full mocks | 2 coding + 2 design + 1 behavioral mock; design EV charging or payment flow; revise story inventory; prioritized gap list |

**Day-30 gate:** Solve a medium-level coding problem in 35-45 minutes with tests and clear complexity; complete a 45-minute design with requirements, sizing, data, failure, security, and observability; deliver six STAR-L stories in under 3 minutes each without unsupported metrics.

## 60-Day Plan: Senior Backend/Platform Readiness

**Outcome:** Add production-depth evidence, reliable technical narratives, and realistic interview-loop stamina. Approximately 190-250 cumulative hours.

| Week | Focus | Required outputs |
| --- | --- | --- |
| 5 | Dynamic programming, graph patterns, union-find/topological sort; Go tests/fuzz/benchmarks | Re-solve misses; 2 timed sessions; fuzz one parser or API boundary |
| 6 | PostgreSQL query plans, locking, isolation, WAL/vacuum, safe migrations; Redis cache/replication | Analyze 3 `EXPLAIN` plans; write migration/backfill/rollback plan; cache failure drill |
| 7 | Kafka ISR, delivery, transactions, rebalances, KRaft, poison events; outbox/CDC/saga | Explain exact-once boundaries; draw DB-broker transactional boundary; simulate duplicate effects |
| 8 | Kubernetes, cloud IAM/networking, deploy/rollback, SLOs, incident response | Troubleshoot a pod/service scenario; define 3 SLIs/SLOs; incident tabletop |

**Day-60 gate:** Three full mock loops across coding, design, and behavior; no repeated high-severity coding mistake; explain service guarantees precisely; all stories show personal actions and outcomes.

## 90-Day Plan: Lead/Staff Differentiation

**Outcome:** Demonstrate cross-team scope, strategy, influence, architecture evolution, and operational leadership. Approximately 290-375 cumulative hours.

| Week | Focus | Required outputs |
| --- | --- | --- |
| 9 | Multi-tenant SaaS, data residency, quotas, deletion, noisy-neighbor isolation | Design one SaaS system from API to operations; tenant-threat model |
| 10 | Platform engineering: internal developer platform, paved roads, adoption, platform SLO | Write an internal platform proposal with user journey and adoption metric |
| 11 | Staff-level architecture: migration strategy, architecture governance, dependencies, ADRs | 2 cross-team design narratives; present options and organizational rollout |
| 12 | AI systems: RAG/agents/MCP basics, evaluations, prompt injection, tool authorization, cost | Design an LLM-backed service with eval harness, permissions, fallback, observability |
| 13 (first 6 days) | Full loop rehearsal, target-company calibration, weakness repair | 3 mock loops; role-specific story mapping; final readiness decision |

**Day-90 gate:** For each target role, map job requirements to 2-3 verified examples. Show one Staff-scope narrative with cross-team outcomes and durability. Complete a system design follow-up on migration, failure, cost, security, and operations without losing the core requirements.

## 180-Day Plan: Broad Product-Company and Specialist Coverage

**Outcome:** Expand depth across specialized role clusters while maintaining interview sharpness. Approximately 570-750 focused hours. Adapt based on actual interview invitations and job descriptions.

| Period | Focus | Outputs |
| --- | --- | --- |
| Weeks 1-4 | 30-day foundation plan | Baseline gates met; identify strongest and weakest interview families |
| Weeks 5-8 | 60-day backend/platform expansion | DB/Kafka/K8s/cloud failure drills; design portfolio |
| Weeks 9-13 | 90-day Staff/AI foundations | Staff stories; platform proposal; AI evaluation design |
| Weeks 14-17 | Deep Go and performance | Runtime, memory, scheduler, pprof/trace, allocation/GC experiments; version-qualified explanations |
| Weeks 18-21 | Deep distributed systems and storage | Raft model, quorum failures, CRDT boundary, replication and sharding; compare DB/Redis/Mongo tradeoffs |
| Weeks 22-24 | Security and cloud architecture | OAuth2/OIDC threat cases; workload identity; supply chain; multi-region/cost review |
| Weeks 25-26 | Role-specific loops and consolidation | Target 3-5 company clusters; recruiter calibration; full mocks; revisit only evidence-based gaps |

Avoid studying a company-specific rumor as fact. Before each real loop, ask the recruiter what competencies, language/tooling, design format, AI-assistance rules, and level expectations will be assessed.

## Hands-On Project for Integrated Practice

Build a small **EV charging session and subscription eligibility service** in Go, sized for learning rather than production claims:

- HTTP or gRPC API with request validation, authentication boundary, idempotency key, and explicit error model.
- PostgreSQL schema for tenant, charging location, session, subscription product, and applicability; constraints and safe migrations.
- Outbox table and Kafka publisher; consumer deduplication; explain transaction boundary and replay behavior.
- Redis cache only for a derived, rebuildable read path; document staleness and invalidation.
- Cancellation/deadlines, bounded worker concurrency, graceful shutdown, retries with jitter and retry budget.
- OpenTelemetry traces, metrics, structured logs with sensitive data redacted; define SLI/SLO and one actionable alert.
- Docker Compose or a local Kubernetes deployment; health/readiness behavior; resource limits and rollback notes.
- Threat model: tenant isolation, token validation, secret handling, replay, injection, and least-privilege service identity.
- Load/chaos tests for DB failure, broker outage, duplicate event, slow dependency, and pod restart.

The project is a learning artifact, not a substitute for claims about professional work. In interviews, be precise about what is implemented, what is simulated, and what remains a design proposal.

## Mock Interview Scorecard

Score each from 1 (weak) to 4 (strong), with one evidence-based note:

| Dimension | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Clarification | Assumes silently | Clarifies late | Gets core constraints | Prioritizes constraints and invariants |
| Correctness | Fails core cases | Partial approach | Correct with prompts | Correct, tested, and robust |
| Communication | Hard to follow | Explains intermittently | Clear and collaborative | Structured, adapts, and leads the discussion |
| Tradeoffs | No alternatives | Names options | Compares meaningful costs | Connects tradeoffs to business/SLO and reversibility |
| Senior impact | Individual task only | Some ownership | End-to-end delivery | Cross-team leverage and durable outcome |
| Production thinking | Happy path | Mentions one failure | Reliability/security/operations covered | Validates recovery, rollout, observability, and cost |

After each mock, choose the lowest two dimensions and schedule the next practice around them. Do not average away a critical correctness or integrity failure.

## Readiness and Reprioritization

- **Green:** Three consecutive mocks meet the relevant role bar, with no recurring correctness/communication failure.
- **Yellow:** One competency is inconsistent; schedule targeted practice and redo the exact miss from a blank start.
- **Red:** Core correctness, unexplained personal contribution, or unsafe production reasoning remains unreliable; delay low-value niche study and repair this first.
- Update the topic priorities weekly from actual job descriptions, recruiter guidance, interview feedback, and local job-market constraints.
