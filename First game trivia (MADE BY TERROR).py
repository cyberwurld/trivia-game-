print('Hello, welcome to trivia! This is a little game i have created just for fun. TYPE THE NAMES HOW THEY ARE IN THE QUESTIONS!!!')

ans = input('Are you ready to play? (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. Who is the stupidest person in the gc? A) sxitch | B) solar | C) naz | D) rot | E) terror | F) Futo : ANSWER = ')
    if ans.lower()  == 'terror':
        score += 1
        print("Correct")
    else:
        print("Incorrect")


ans = input('2. who made up the word "SHICH YE?" A) sxitch | B) solar | C) naz | D) rot | E) terror | F) Futo : ANSWER = ')
if ans.lower()  == 'rot':
    score += 1
    print("Correct")
else:
    print("Incorrect")


ans = input('3. who will win in a 1v1 in basketball? A) sxitch VS B) terror : ANSWER = ')
if ans.lower()  == 'terror':
    score += 1
    print("Correct")
else:
    print("Incorrect")

ans = input('4. who can bake the most? A) sxitch | B) solar | C) naz | D) rot | E) terror | F) Futo : ANSWER = ')
if ans.lower()  == 'sxitch':
    score += 1
    print("Correct")
else:
    print("Incorrect")

print('Thank you for playing this game! you got ', score, "questions correct.")
player = (score/total_q) * 100

print("player: ", player)
print()