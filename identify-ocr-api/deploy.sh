GOOGLE_PROJECT_ID=# Google Cloud Platform Project ID

gcloud builds submit --tag gcr.io/$GOOGLE_PROJECT_ID/ocr-api \
  --project=$GOOGLE_PROJECT_ID

gcloud beta run deploy ocr-api \
  --image gcr.io/$GOOGLE_PROJECT_ID/ocr-api \
  --platform managed \
  --region asia-southeast2 \
  --project=$GOOGLE_PROJECT_ID \
  --allow-unauthenticated