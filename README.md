# spotify-datapipeline-python

Spotify datapipeline python

# Description
* Create a client id and secret id in spotify developer API
* Using that API, we take the top 100 playlist in json format.
* Use extract lambda functiona that connects to API and uploads  the raw json files in S3 
* Then with another lamda function transform the json into readable csv files.
* Upoad the transformed csv files into S3 bucket.

# Architecture
![image](https://github.com/user-attachments/assets/281facb3-fda3-4e12-b6c2-576997bce63d)
