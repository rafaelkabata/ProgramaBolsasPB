
max_movies = 0
max_actor = ''
total_gross = 0
num_movies = 0
max_average_per_movie = 0
max_average_actor = ''
movie_count = {}
actors_gross = []

with open('actors.csv', 'r') as file:
    
    next(file)
  
    for line in file:
        
        line = line.strip()
        
        corrected_line = line.replace('"', '').replace('Robert Downey, Jr.', 'Robert Downey Jr')
        
        fields = corrected_line.split(',')
        
        if len(fields) >= 6:
            
            gross = float(fields[5])  
            total_gross += gross
            
            num_movies += 1
            
            if fields[2].isdigit():
                
                num_movies_actor = int(fields[2])
                
                if num_movies_actor > max_movies:
                    max_movies = num_movies_actor
                    max_actor = fields[0]
            
            average_per_movie = float(fields[3])  
            
            if average_per_movie > max_average_per_movie:
                max_average_per_movie = average_per_movie
                max_average_actor = fields[0]
            
            movie = fields[4]  
           
            movie_count[movie] = movie_count.get(movie, 0) + 1
            
            actor = fields[0]  
            
            total_gross_actor = float(fields[1])  
           
            actors_gross.append((actor, total_gross_actor))


average_gross = total_gross / num_movies

sorted_movies = sorted(movie_count.items(), key=lambda x: (-x[1], x[0]))

actors_gross.sort(key=lambda x: x[1], reverse=True)

with open('etapa_01.txt', 'w') as output_file:
    output_file.write(f"O ator/atriz com o maior número de filmes é: {max_actor}, com um total de {max_movies} filmes.\n")

with open('etapa_02.txt', 'w') as output_file:
    output_file.write(f"A média da receita de bilheteria bruta dos principais filmes é: ${average_gross:.2f}.\n")

with open('etapa_03.txt', 'w') as output_file:
    output_file.write(f"O ator/atriz com a maior média de receita de bilheteria bruta por filme é: {max_average_actor}, com uma média de ${max_average_per_movie:.2f} por filme.\n")

with open('etapa_04.txt', 'w') as output_file:
    for movie, count in sorted_movies:
        output_file.write(f"Filme {movie} aparece {count} vezes no dataset.\n")

with open('etapa_05.txt', 'w') as output_file:
    for actor, gross in actors_gross:
        output_file.write(f"{actor} - {gross}\n")
