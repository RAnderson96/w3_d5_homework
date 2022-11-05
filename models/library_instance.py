
from models.library import Library


blurb1 = "Two hundred years after migrating into space, mankind is in turmoil. When a reluctant ship's captain and washed-up detective find themselves involved in the case of a missing girl, what they discover brings our solar system to the brink of civil war, and exposes the greatest conspiracy in human history"
blurb2 = "The first part of J R R Tolkien's epic masterpiece The Lord of the Rings, this is the story of young hobbit Frodo Baggins, who finds himself faced with an immense and terrible duty. Sauron has gathered to him all the Rings of Power, and intendes to use them to rule Middle-earth."
blurb3 = "So begins the tale of Kvothe - currently known as Kote, the unassuming innkeepter - from his childhood in a troupe of traveling players, through his years spent as a near-feral orphan in a crime-riddled city, to his daringly brazen yet successful bid to enter a difficult and dangerous school of magic."
blurb4 = "In Immune, Philipp Dettmer, the brains behind the most popular science channel on YouTube, takes readers on a journey through the fortress of the human body and its defences. There is a constant battle of staggering scale raging within us, full of stories of invasion, strategy, defeat, and noble self-sacrifice."




book_1 = Library("The Name of the Wind", "Patrick Rothfuss", "Fantasy", blurb3)
book_2 = Library("The Fellowship of the Ring", "J.R.R Tolkien", "Fantasy", blurb2)
book_3 = Library("Leviathan Wakes", "James S.A. Corey","Science-Fiction", blurb1)
book_4 = Library("IMMUNE", "Philipp Dettmer", "Medical Non-Fiction", blurb4)

books = [book_1, book_2, book_3, book_4]

blurb5 = "Shallan, a minor lighteyed woman whose family and lands are in danger, hatches a daring plot to switch a broken Soulcaster (a device that allows people to change objects to other things) with a working one belonging to Jasnah Kholin, sister of the Alethi king."
book_5 = Library("The Way of Kings", "Brandon Sanderson", "Fantasy", blurb5)

blurb6 = "The Colour of Magic is a collection of four stories set on Discworld, a flat planet that is carried by four huge elephants that stand on the back of the giant turtle Great A'Tuin. The stories pivot on the hapless failed wizard Rincewind."
book_6 = Library("The Colour of Magic", "Terry Pratchett", "Fantasy", blurb6)


books = [book_1, book_2, book_3, book_4, book_5, book_6]

def add_book_to_list(new_book):
    books.append(new_book)

def remove_book_from_list(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete=book
            break

    books.remove(book_to_delete)

def checkout_book(book_title):
    for book in books:
        if book.title == book_title:
            if book.checked_out==False:
                book.checked_out=True
                break
            elif book.checked_out==True:
                book.checked_out=False
                break