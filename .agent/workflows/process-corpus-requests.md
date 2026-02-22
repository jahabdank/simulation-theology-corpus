---
description: Process User Requests and Update Corpus
---

# Process Corpus Requests

This workflow executes an automated processing loop. The goal is to process new inputs from the `/user-requests` folder, update the Simulation Theology corpus accordingly, and generate the necessary artifacts (release notes and dilemma logs).

## Note the folder structure:
/agent-log - for logging of agentic activities as defined by the agent-logging.md workflow
/corpus - the full corpus of the Simulation Theology, with graph style knowledge structure
/user-core-archive - an archive of texts which are the basis for creation of the ST corpus
/user-requests-processed - an archive of RLHF responses by human to the change requests, as a supplemaentary data to fine tune the corpus. All docuemnts here were already prpocessed, they are historical archive
/user-requests - a list of change requests by the userthat have to be implemented in the current revision of the corpus 
/questions-dillemas - a folder with AI generated questions and dillemas that need to be answer by human. When human answers the questions, they would move the file populated with the answers into the /user-requests-unprocessed folder for next rounds of processing

## Steps

1. **Verify State:** Check the `/user-requests/` directory. If empty, the workflow terminates successfully.
2. **Read Requests:** Read the contents of all markdown files inside `/user-requests/`. Read the files in the `/corpus/` directory to understand the current state.
3. **Execute Updates:** For each user request in the /user-requests/ file:
   - Carefully interpret the request and logically determine which files in the `/corpus/` directory need to be updated, or if new files need to be created. User requests might relate to the text of the element in a nuanced manner, therefore be thoughtful and comprehensive about these updates. Even if user specifically addresses one element that needs to be changed, it is your job to cross reference other items so ensure cosistancy of the corpus. You are only allowed to skpi this if use explicitly tells you to make change only to the one item he chooses. Else overall consistency is paramount
   - For every modified or newly created corpus file, process the text and **maintain the following three marker sections at the very bottom of the file** (append them if they do not exist, or update them if they do):
     - `### Summary of changes`: A brief explanation of what was altered and why.
     - `### New ideas introduced`: (If applicable) Bullet points of novel concepts added that were not present previously.
     - `### Questions and dillemas for user`: Any contradictions spotted or questions you have regarding the revisions made to this specific item that use should clarify in the next iteration
4. **Generate Artifacts & Logs:**
   - Compile a comprehensive release note document summarizing the entire processing pass. Save this document in `/release-notes/`.
   - Iterate over all the corpus items that were updated. Aggregate all the questions from the `### Questions and dillemas for user` sections into a single summary file.
   - Save this summary file in the `/questions-dillemas/` folder. The filename MUST be prepended with a full creation timestamp in the format `YYYYMMDD_HHMMSS` (e.g., `YYYYMMDD_HHMMSS_dilemmas.md`).
5. **Archive Requests:** 
   - Move all processed request files from `/user-requests/` to `/user-requests-archive/`.