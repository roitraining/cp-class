# Vertex Search

## Setup

1. Configure the Google Cloud SDK to point to the classroom project
2. Clone this repo
3. Deploy the index to an endpoint (sub values for placeholders). This should
   be done the morning of the last day (when the students will be doing
   the embeddings lab); you don't want to create this endpoint and leave
   it laying around for multiple days.

   ```bash
   cd cp-class/instructor
   export PROJECT_ID="class-project-id"
   export INITIALS="your-initials"
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python v-setup.py
   ```

   This process will take 20-30 minutes to finish

4. Copy the `endpoint_id` and `deployed_index_id` to a file so you can share 
   with students later

## Cleanup

Do cleanup at the end of the day where the students do the embeddings lab.
Also, make sure no one else is running the class. If someone is, leave the
cleanup to the last person running the class that day.

1. Undeploy the model and remove the endpoint.
   ```bash
   export PROJECT_ID="class-project-id"
   python v-clean.py
   ```