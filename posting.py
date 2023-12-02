import os
import sys
from datetime import datetime

def create_new_post(title):
    # Set the path to the _posts directory
    posts_directory = "_posts"

    # Convert title to camel case and remove hyphens
    camel_case_title = ' '.join(word.capitalize() for word in title.split('-'))

    # Generate the filename based on the current date and post title
    date_prefix = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_prefix}-{title.lower().replace(' ', '-')}.md"

    # Set the full path to the new post file
    post_path = os.path.join(posts_directory, filename)

    # Create the new post file with front matter
    with open(post_path, "w") as file:
        file.write(f"---\n")
        file.write(f"layout: post\n")
        file.write(f"title: \"{camel_case_title}\"\n")
        file.write(f"date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')}\n")
        file.write(f"categories: []\n")  # Add categories as needed
        file.write(f"---\n\n")
        file.write(f"New Post! .\n")

    print(f"New post created: {post_path}")

    # Open the new post file in the default text editor
    try:
        os.system(f"code {os.path.abspath(post_path)}")
    except Exception as e:
        print(f"Error opening the text editor: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_post.py 'Your Post Title'")
    else:
        post_title = sys.argv[1]
        create_new_post(post_title)
