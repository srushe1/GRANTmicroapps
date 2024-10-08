APP_TITLE = "Future Funding Draft Feedback"
APP_INTRO = """This is a template for an AI-powered Microapp that scores a learner's future funding draft against a checklist."""

APP_HOW_IT_WORKS = """
This AI-Powered Microapps work by scoring the learner input against the checklist. 

Please review the provided future funding draft and provide feedback based on the following rubric.
Rubric:
**Done well: The item fully addresses the criterion.
**Needs improvement: The item partially addresses the criterion.
**Not included: The item does not address the criterion.
Criteria to be scored:
**Do you provide a plan for necessary funding beyond the grant period of your proposal?
**Does the plan introduce new partners or expansion of funding opportunities?
**Have you considered inflationary factors or new equipment or operational needs for the next phase?
**Does this component show you will diversify your funding strategy?
**Will future funding include being more self-sufficient or increase local support?
**Is this section summarized versus being as detailed as the budget for the year of funding of the proposal?



 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = "Please review the provided future funding draft and provide feedback according to the following rubric. Prioritize the feedback you provide based on the rubric but don't show the user the rubric or any score give."

PHASES = {
    "phase1": {
        "name": "Future Funding Draft",
        "fields": {
            "futurefunding_draft": {
                "type": "text_area",
                "height": 400,
                "label": """Please paste your Future Funding Draft""",
                "value": ""
            }
        },
        "phase_instructions": "",
        "user_prompt": """Simply read my text and provide brief feedback and a score based on the following rubric:
        
        **Rubric:**
            2 points - Done well: The item fully addresses the criterion.
            1 point - Needs improvement: The item partially addresses the criterion.
            0 points - Not included: The item does not address the criterion.
            
        **Criteria to be scored:**
            1. Do you provide a plan for necessary funding beyond the grant period of your proposal?
            2. Does the plan introduce new partners or expansion of funding opportunities?
            3. Have you considered inflationary factors or new equipment or operational needs for the next phase?
            4. Does this component show you will diversify your funding strategy?
            5. Will future funding include being more self-sufficient or increase local support?
            6. Is this section summarized versus being as detailed as the budget for the year of funding of the proposal?


            
        Provide a paragraph stating what they did well and feedback for only two criteria that could be improved.

        **Text:**
        {futurefunding_draft}
        """,
        "allow_skip": False,
       
    }
}




PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope this feedback helps you to review your evaluation draft. Be sure to continue to refine before you submit."
COMPLETION_CELEBRATION = False
