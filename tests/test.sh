curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.\n    Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2005217@ds.study.iitm.ac.in\n    What is the JSON output of the command? (Paste only the JSON body, not the headers)" \
