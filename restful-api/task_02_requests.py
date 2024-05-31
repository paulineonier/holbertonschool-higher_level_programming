import requests
import csv

def fetch_and_print_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print status code of the response
    print("Status Code:", response.status_code)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse fetched data into a JSON object
        posts = response.json()
        
        # Iterate through parsed JSON data and print titles of all posts
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse fetched data into a JSON object
        posts = response.json()
        
        # Structure data into a list of dictionaries
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Write data into a CSV file
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
                
        print("Posts saved to posts.csv")
