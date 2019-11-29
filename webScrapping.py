from requests import get
from bs4 import BeautifulSoup

pages = [str(i) for i in range(1,5)]
year = str(input("input movie year you want to: "))

 # Lists to store the scraped data in

genres = []
imdb_ratings = []
metascore = []
votes = []
names = []

for page in pages:

        response = get("http://www.imdb.com/search/title?release_date="+year+"&sort=num_votes,desc&page="+page)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
       
        # Extract data from individual movie container
        for container in movie_containers:
        # If the movie has Metascore, then extract:
                if container.find('div', class_ = 'ratings-metascore') is not None:
                # The name
                        name = container.h3.a.text
                        names.append(name)
                # The IMDB rating
                        imdb = float(container.strong.text)
                        imdb_ratings.append(imdb)
                # The Metascore
                        m_score = container.find('span', class_ = 'metascore').text
                        metascore.append(int(m_score))
                # The number of votes
                        vote = container.find('span', attrs = {'name':'nv'})['data-value']
                        votes.append(int(vote))
                # The genre
                        gnr = container.find('span', class_ = 'genre').text
                        genres.append(gnr[1:-12])

#Create txt file to catch the information
file = open("Result.txt", "w")
opening = "Best Movies released in "+year+"\n\n"
finalString = ""
for i in range(len(names)):
        finalString += str(i+1)+". "+names[i]+"\nGenre   : "+genres[i]+"\nRating  : "
        finalString += str(imdb_ratings[i])+"\nMetascore : "+str(metascore[i])+"\nVotes : "+str(votes[i])+"\nDescription : " +"\n\n"
finalString = opening+finalString;
file.write(finalString)
file.close()



