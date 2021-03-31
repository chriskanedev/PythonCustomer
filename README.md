# Café

Here's the link to our [Jira Kanban Board][1]

[1]: https://2608436.atlassian.net/secure/RapidBoard.jspa?rapidView=1&projectKey=CAFE

when moving a file to new location in the reposity git bash loses the tracking of it it needs to be readded and added under its new path
e.g test.txt is moved into testing folder from being in the same directory as the folder you need to add test.txt and testing\test.txt
if moved into a gui folder in testing this would be testing\gui\test.txt

files using relative paths to denote moving up a level use ..\ (\\ to stop escape characters) moving two levels up is ..\..\ then you put the file path from that point

If project is configured to master folder miss out any ..\'s and just path to the required point
#this is prefered
