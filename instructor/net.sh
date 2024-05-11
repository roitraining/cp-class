#!/bin/bash

echo "Please choose the ingress setting:"
echo "1) All"
echo "2) Internal"

read -p "Enter your choice (1 or 2): " choice

case $choice in
  1)
    INGRESS=all
    ;;
  2)
    INGRESS=internal
    ;;
  *)
    echo "Invalid choice. Defaulting to 'internal'."
    INGRESS=internal
    ;;
esac

gcloud run services update assign-a-role --ingress $INGRESS --region=us-central1