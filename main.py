from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import re

# 1. Extract video ID from URL
def extract_video_id(url: str) -> str:
    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

# 2. Fetch the transcript
def get_transcript(video_id: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([item["text"] for item in transcript])

# 3. Summarize using OpenAI
def summarize_text(text: str) -> str:
    client = OpenAI()       # reads APIkey from environment variable OPENAI_API_KEY
    prompt = f"Summarize the following YouTube video transcript in 5 concise bullet points:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# 4. Run it
if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    video_id = extract_video_id(url)
    print("\nExtracting transcript...")
    transcript_text = get_transcript(video_id)

    print("\nGenerating summary...")
    summary = summarize_text(transcript_text)

    print("Summary:\n")
    print(summary)