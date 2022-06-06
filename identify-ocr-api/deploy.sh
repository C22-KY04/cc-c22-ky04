GOOGLE_PROJECT_ID=# Google Cloud Platform Project ID

gsutil cp gs://idcard-identification-models/model.h5 ./modules/identify/

gcloud builds submit --tag gcr.io/$GOOGLE_PROJECT_ID/identify-ocr-api \
  --project=$GOOGLE_PROJECT_ID

gcloud beta run deploy ocr-api \
  --image gcr.io/$GOOGLE_PROJECT_ID/identify-ocr-api \
  --platform managed \
  --region asia-southeast2 \
  --project=$GOOGLE_PROJECT_ID \
  --allow-unauthenticated