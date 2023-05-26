movie_user={"the race","olive","room345"}
user_ip=input("Enter the movie watched: ").lower()
if user_ip in movie_user:
    print(f"I have watched {user_ip} movie")
else:
    print("i haven't watched this movie once!!")