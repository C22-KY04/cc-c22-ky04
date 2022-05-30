GOOGLE_PROJECT_ID=# Google Cloud Platform Project ID

gcloud builds submit --tag gcr.io/$GOOGLE_PROJECT_ID/idcards-api \
  --project=$GOOGLE_PROJECT_ID

gcloud beta run deploy idcards-api \
  --image gcr.io/$GOOGLE_PROJECT_ID/idcards-api \
  --platform managed \
  --region asia-southeast2 \
  --project=$GOOGLE_PROJECT_ID \
  --allow-unauthenticated
