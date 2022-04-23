from app import db
from models import Pet  

db.drop_all()
db.create_all()

p1 = Pet(
    name="Coco", 
    species="dog",
    photo_url="https://hellobark.com/wp-content/uploads/irish-doodle-tongue-out.jpg",
    age="4",
    notes="Play Dead sit nap lazy dog wet nose Tigger run fast fish lazy cat wagging hamster toy field yawn feathers ferret yawn aquarium.Feathers bird seed food scratcher mouse running teeth licks heel walk pet gate maine coon cat collar twine parakeet. Roll Over kitty barky critters litter stick window litter box wagging field toy. Whiskers harness biscuit food lick small animals throw meow house train."
    )

p2 = Pet(
    name="Gertrude", 
    species="guinea pig",
    photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/George_the_amazing_guinea_pig.jpg/640px-George_the_amazing_guinea_pig.jpg",
    age="2",
    notes="Bedding field hamster small animals carrier polydactyl groom vaccine. Commands running gimme five groom slobber run fast head ball litter box biscuit catch run fast roll over. Roll Over litter box tabby pet slobbery play dead kitty roll over small animals barky good boy string kitty fish licks teeth chew drool. ID Tag barky lick parakeet wet nose ball walk tabby wag tail chirp nest."
    )

p3 = Pet(
    name="Oreo", 
    species="cat",
    photo_url="https://i.pinimg.com/736x/9d/99/ca/9d99ca44faa65e9a9914c7c6715c28e3.jpg",
    age="9",
    notes="Maine Coon Cat walk catch water dog slobber chew scratcher ID tag litter tuxedo dog house lazy cat park. Dinnertime fetch throw feathers fleas tongue lazy cat lick throw kitten parrot hamster wag tail aquarium chew heel good boy lick feathers cockatiel. Wet Nose food ferret vaccine finch vaccination Scooby snacks string wagging barky tail head good boy pet gate meow good boy."
    )

p4 = Pet(
    name="Molly", 
    species="dog",
    photo_url="https://www.cesarsway.com/wp-content/uploads/2019/07/AdobeStock_190562487.jpeg",
    age="1",
    notes="Good Boy park lazy dog walk kibble Scooby snacks licks canary. Wet Nose food ferret vaccine finch vaccination Scooby snacks string wagging barky tail head good boy pet gate meow good boy. Commands shake bird biscuit left paw finch bark ferret bark gimme five turtle fur canary. Water puppy dog lick kisses pet supplies slobber cat bird seed. Food sit biscuit groom tongue cage."
    )



db.session.add_all([p1, p2, p3, p4])
db.session.commit()