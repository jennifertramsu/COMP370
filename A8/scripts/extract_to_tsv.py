import argparse
from os import name
import pandas as pd
import json
import random
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', required=True, help="Output file")
    parser.add_argument('json_file', help="Input JSON file")
    parser.add_argument('num_posts_to_output', type=int, help="Number of posts to output")
    args = parser.parse_args()

    out = Path("../data/" + args.output)
    json_file = args.json_file
    num_posts_to_output = args.num_posts_to_output

    # Read in file
    with open(json_file) as f:
        data = json.load(f)
        posts = data['data']['children']

    # Create dataframe
    df = pd.DataFrame(columns=['Name', 'title', 'coding'])

    if num_posts_to_output >= len(posts):
        for post in posts:
            name = post['data']['name']
            title = post['data']['title']
            coding = None
            row = pd.DataFrame({'Name': name, 'title': title, 'coding': coding}, index=[0])
            df = pd.concat([df, row], ignore_index=True)
    else:
        rand = []
        for i in range(num_posts_to_output):
            idx = random.randint(0, len(posts)-1)
            
            if idx not in rand:
                rand.append(idx)
            else:
                while idx in rand:
                    idx = random.randint(0, len(posts)-1)
                rand.append(idx)

            post = posts[idx]
            name = post['data']['name']
            title = post['data']['title']
            coding = None
            row = pd.DataFrame({'Name': name, 'title': title, 'coding': coding}, index=[0])
            df = pd.concat([df, row], ignore_index=True)

    # Saving file
    df.to_csv(out, sep='\t', index=False)

if __name__ == '__main__':
    main()