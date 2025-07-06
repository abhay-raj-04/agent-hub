```mermaid
---
config:
  flowchart:
    curve: linear
---
graph TD;
	__start__([<p>__start__</p>]):::first
	ingest_documents(ingest_documents)
	router(router)
	analyze_resume(analyze_resume)
	generate_quiz(generate_quiz)
	rewrite_section(rewrite_section)
	format_output(format_output)
	__end__([<p>__end__</p>]):::last
	__start__ --> ingest_documents;
	analyze_resume --> format_output;
	generate_quiz --> format_output;
	ingest_documents --> router;
	rewrite_section --> format_output;
	router -. &nbsp;END_CONVERSATION&nbsp; .-> __end__;
	router -. &nbsp;ANALYZE&nbsp; .-> analyze_resume;
	router -. &nbsp;GREETING/INFO&nbsp; .-> format_output;
	router -. &nbsp;QUIZ&nbsp; .-> generate_quiz;
	router -. &nbsp;REWRITE&nbsp; .-> rewrite_section;
	format_output --> __end__;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
