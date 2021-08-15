transcriptFileUri = "https://s3.ap-southeast-2.amazonaws.com/pexa-audio-analysis-poc/transcribe_output/pexa-transcribe-lambda-trigger-Thu-12-Aug-gmt-2021-08-06-19.json"

print(transcriptFileUri.split('/')[-1])
print(transcriptFileUri.split('/')[-2])
print(transcriptFileUri.split('/')[-3])