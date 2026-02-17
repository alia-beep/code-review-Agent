import os
from github import Github
from openai import OpenAI
from dotenv import load_dotenv

# 1. Environment variables load karein (.env file se)
load_dotenv()

# 2. ScaleDown AI Client setup
# ScaleDown aksar OpenAI ka format use karta hai isliye hum OpenAI library use kar rahe hain
client = OpenAI(
    api_key=os.getenv("SCALEDOWN_API_KEY"),
    base_url=os.getenv("SCALEDOWN_BASE_URL")
)

def get_ai_review(code_diff):
    """
    ScaleDown API ko code bhej kar review mangna
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Agar ye model na chale toh "gemini-1.5-flash" try karein
            messages=[
                {
                    "role": "system", 
                    "content": "You are a Senior Software Engineer. Review the code diff for bugs, security issues, and clean code. Be concise."
                },
                {
                    "role": "user", 
                    "content": f"Review this code change:\n\n{code_diff}"
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Review error: {str(e)}"

def start_review():
    # 3. GitHub Connection
    g = Github(os.getenv("GITHUB_TOKEN"))
    
    # User se input lein
    repo_name = input("Enter Repo Name (e.g., username/repository): ")
    pr_number = int(input("Enter Pull Request Number: "))

    try:
        repo = g.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        
        print(f"🔍 Fetching code for PR #{pr_number}...")
        
        files = pr.get_files()
        
        for file in files:
            if file.patch: # Sirf un files ko check karein jisme badlav (diff) hai
                print(f"🛠️ Reviewing {file.filename}...")
                
                # AI se review lein
                review_comment = get_ai_review(file.patch)
                
                # 4. GitHub par comment post karein
                formatted_comment = f"### 🤖 AI Code Review for `{file.filename}`\n\n{review_comment}"
                pr.create_issue_comment(formatted_comment)
                
                print(f"✅ Review posted for {file.filename}")
        
        print("\n🎉 All files reviewed successfully!")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    start_review()