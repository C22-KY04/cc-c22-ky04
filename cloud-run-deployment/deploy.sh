GOOGLE_PROJECT_ID=# Google Cloud Platform Project ID

gcloud builds submit --tag gcr.io/$GOOGLE_PROJECT_ID/idcardsapi \
  --project=$GOOGLE_PROJECT_ID

gcloud beta run deploy barkbark-api \
  --image gcr.io/$GOOGLE_PROJECT_ID/idcardsapi \
  --platform managed \
  --region asia-southeast2 \
  --project=$GOOGLE_PROJECT_ID