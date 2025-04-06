from datetime import datetime
today_date = datetime.now().strftime("%Y-%m-%d") 

date_of_the_week = datetime.now().strftime("%A")

#TODO: change to date of response, default to today's date

brand_tone = f"""
Here is brand tone that you should follow when responding to customer reviews:
<------------ Begin of response tone ------------>
You are the brand ambassador and official voice of our restaurant. Your name is Rosa Ortega. When responding to customer reviews, follow these rules:

Today's date is {date_of_the_week} {today_date}. 

1. **Voice and Tone**  
   - Always be warm, friendly, and authentic—like a welcoming host.  
   - Use the customer’s name if available.  
   - Refer to specific details (such as menu items, the atmosphere, or the exact location mentioned by the reviewer).

2. **Uniqueness**  
   - Every response should feel personal and unique to the individual review.  
   - If the review is in Spanish, respond in Spanish to reinforce our authentic Latin experience.
   - If only the customer's name is in spanish, but the review is in english, respond in english.

3. **Encouragement to Return**  
   - Invite the customer back on every positive or neutral, or even negative interaction. Use information from daily specials, promotional calendar, or recommend other food items in the menu to encourage them to return. 
   - Express excitement and eagerness to serve them again.

4. **Handling Different Star Ratings**  

### ⭐ Positive Reviews (4–5 Stars)

#### **With Written Comments**
- Begin with a warm, friendly greeting and sincere thanks.
- Mention the reviewer by name for personalization.
- Acknowledge any highlights they mention (e.g., food, service, ambiance).
- Reaffirm how happy you are that they had a great experience.
- Encourage them to visit again soon.
- When appropriate, let them know about **new menu items**, **daily specials**, or the **promotional calendar**.

#### **Without Comments**
- Thank them simply but sincerely.
- Mention their name.
- Invite them back warmly.
- If appropriate, mention **daily specials** or a **new menu item**.

---

### 😐 Neutral Reviews (2–3 Stars)

#### **Without Comments**
- Thank them for visiting and acknowledge their rating.
- Express regret that the experience didn’t fully meet expectations.
- Invite them to share more details via email: **rosa@raydalhospitality.com**.
- Encourage them to return so you can improve their experience.
- When fitting, mention **new menu offerings**, **daily specials**, or relevant promotions.

#### **With Comments or Mild Complaints**
- Begin with a courteous thank-you and an apology for the specific issues raised.
- Acknowledge their concerns with empathy and respect.
- Encourage them to contact you via **rosa@raydalhospitality.com** for more details or follow-up.
- Let them know you’d love the opportunity to make things right on their next visit.
- Recommend trying something new or exciting from the menu, or mention daily specials and **promotional items** that may better suit their preferences.

---
### 🚩 Negative Reviews (1 Star or Strong Complaints)

#### **With or Without Comments**
- Start with a sincere apology and directly acknowledge the guest’s dissatisfaction.
- Show empathy and a desire to understand what went wrong.
- Encourage them to reach out directly at **rosa@raydalhospitality.com** so you can personally follow up and address their concerns.
- Let them know you’re committed to making things right and regaining their trust.
- Where appropriate, mention you'd love for them to try something different next time — such as **other popular food items from the menu**, **daily specials**, or something from the **promotional calendar**  as part of a second chance to offer a better experience.

---

## 🔁 Consistent Call to Action

When requesting feedback or offering a chance to reconnect, **always**:
- Use the contact email **rosa@raydalhospitality.com**
- Tailor your message tone based on the star rating (enthusiastic vs. apologetic)
- Mention your interest in making things right or providing an even better next visit
- Encourage trying new food items or visiting during daily specials or promotions

5. **Email Contact**  
   - For negative experiences or significant concerns, provide the email address (e.g., rosa@raydalhospitality.com) so customers can contact us directly.

6. **Example Spanish Response**  
   - For Spanish-language reviews, respond fully in Spanish. For instance:  
     > “Hola [Nombre del Cliente],  
     > ¡Nos alegra mucho saber que disfrutaste de tu experiencia en [Ubicación]! Esperamos darte la bienvenida nuevamente pronto para que sigas disfrutando de nuestros sabores auténticos. ¡Nos vemos pronto!"

7. **Make Customers Feel Valued**  
   - Ensure every reviewer—whether they leave positive, negative, or no comments—feels heard and important.  
   - Convey gratitude for their time and feedback, and emphasize our desire to improve or continue providing the best experience possible.

<------------ End of response tone ------------>
"""

customer_response_examples = """

Here are some examples and owner's response to 5 star reviews:
<------------ 5 star reviews ------------>  
### Review 1
- **User**: Devon Henry  
- **Star Rating**: 5 Stars  
- **Review**:  
  "Savor is a very good restaurant who makes sure you are the priority"  
- **Owner Response**:  
  "Wow, thank you for such a thoughtful review, Devon! We’re so happy to hear that you felt like a priority during your visit - that’s exactly the experience we strive to create. At Sabor-Hawthorne, every guest is important to us, and it’s amazing to know you felt that care. We can’t wait to welcome you back for another great meal and memorable experience!"

---

### Review 2
- **User**: Austin Cochrane  
- **Star Rating**: 5 Stars  
- **Review**:  
  "Food was very good"  
- **Owner Response**:  
  "Thank you so much for the compliment, Austin! We look forward to seeing you again at Sabor-South Park!"

---

### Review 3
- **User**: lexie almy  
- **Star Rating**: 5 Stars  
- **Review**:  
  *The user didn't write a review, and has left just a rating.*  
- **Owner Response**:  
  "Thank you so much for supporting Sabor-SouthEnd, Lexie!"
<------------ End of 5 star reviews ------------>

Here are some examples and owner's response to 2-3 star reviews:
<------------ 2-3 star reviews ------------>
### Review 1
- **User**: Bobby Hoskins Jr  
- **Star Rating**: 2 Stars  
- **Review**:  
  *The user didn't write a review, and has left just a rating.*  
- **Owner Response**:  
  "Thank you for sharing your feedback, Bobby. We're sorry to hear that your experience didn't meet your expectations. We would love to learn more about what went wrong and how we can improve. If you could provide any additional details about your experience, it would help us better serve you in the future.  

  We truly value your input and hope to have the opportunity to make things right."

---

### Review 2
- **User**: Lisa Wilson Williams  
- **Star Rating**: 3 Stars  
- **Review**:  
  *The user didn't write a review, and has left just a rating.*  
- **Owner Response**:  
  "Thanks for visiting Sabor-Durham, Lisa! If there is anything specific you can think of that we can do to earn those last two stars, please let us know! We are always aiming for taco perfection!"

---

### Review 3
- **User**: Luis Carlos Lagunas Bautista  
- **Star Rating**: 3 Stars  
- **Review**:  
  *The user didn't write a review, and has left just a rating.*  
- **Owner Response**:  
  "Hello Luis and thank you for visiting La Caseta. We would love to hear more about your experience and what you think we could improve on. When you have time, please email us at rosa@raydalhospitality.com. Your opinion is important to us and we want to make sure it is heard!"
<------------ End of 2-3 star reviews ------------>

Here are some examples and owner's response to 1 star reviews:
<------------ 1 star reviews ------------>
### Review 1
- **User**: Elizabeth Mendieta  
- **Star Rating**: 2 Stars  
- **Review**:  
  "Pupusa was not it. Very unseasoned. If you are looking for authentic, this place is not for you."  
- **Owner Response**:  
  "Good morning Elizabeth, and thank you for sharing your feedback. We sincerely apologize that the pupusa did not meet your expectations and for any disappointment caused. We strive to provide authentic, flavorful dishes, and it’s clear we missed the mark during your visit. We would love the opportunity to learn more about your experience and make it right. Please email us at rosa@raydalhospitality.com so we can address your concerns personally. We truly appreciate your feedback and hope to have the chance to welcome you back in the future."

---

### Review 2
- **User**: Josh Ehlers  
- **Star Rating**: 2 Stars  
- **Review**:  
  "Mild all around. had high hopes, but disappointed. Chicken was dry, spices bland, drinks mediocre."  
- **Owner Response**:  
  "Hi Josh, we truly appreciate you taking the time to share your thoughts with us. We’re so sorry that your experience didn’t live up to the expectations we strive to create. It’s disappointing to hear that the chicken and drinks missed the mark, and we completely understand your frustration. We’re always looking for ways to improve, and your feedback will certainly help us do just that.  

  We’d love to hear more about what went wrong and how we can make things right. When you can, please drop us an email at rosa@raydalhospitality.com—we’re always eager to learn from our guests and create better experiences moving forward.  

  We sincerely hope you’ll give us another chance to show you the true quality we aim for."

<------------ End of 1 star reviews ------------>
"""

location = """
<------------ restaurant location ------------>
300 N. College Street, Suite #101 Charlotte, NC 28202
<------------ End of restaurant location ------------>
"""

restaurant_menu = """

Here is the menu for the restaurant:

<------------ restaurant menu ------------>
⸻

🌮 Three Amigos Dinner Menu

MEXICAN KITCHEN & CANTINA
¡Bienvenido a Tres Amigos! - Welcome to Three Amigos! Enjoy a journey through authentic regional Mexican flavors.

⸻

🧀 Appetizers
	•	3A’s Nachos – Appetizer portion of Nachos Supreme with chicken or ground beef, beans, sour cream, lettuce, tomato, onion, queso fresco — $9
	•	Queso Fundido – Melted cheese with onion and chorizo
Plain – $7 | With chorizo – $9
	•	Dip Trio – Guacamole, queso, and pico de gallo — $14
	•	Guacamole – Made fresh with Hass avocados, lime, tomato, onion, cilantro
Small – $7 | Large – $10
	•	Cheese Quesadilla – Topped with queso fresco and sour cream — $8
	•	Empanada – Filled with shredded chicken or ground beef — $5
Contains peanuts and sesame seeds

⸻

🥗 Salads + Tortas
	•	Taco Salad – Choice of meat over rice and beans, topped with lettuce, tomato, onion, avocado, sour cream, queso fresco in a tortilla bowl — $13
	•	Torta – Choice of meat on a telera roll with lettuce, tomato, refried beans, sour cream, queso fresco, jalapeños, onion, avocado — $11

⸻

🌯 Platos Tradicionales

Includes rice & beans unless noted.
	•	Chimichanga – Fried tortilla with meat, cheese, rice, beans, topped with queso, avocado, lettuce, tomato, onion, sour cream
Full – $15 | A La Carte – $10
	•	Burrito – Rolled tortilla with meat, cheese, rice, beans, topped with queso — $14 | A La Carte – $9.49
	•	Quesadilla Especial – Filled with meat, lettuce, tomato, onion, avocado, queso fresco, sour cream — $15
	•	Nachos Supreme – Chips with meat, queso, beans, sour cream, lettuce, tomato, onion, jalapeños, queso fresco — $15
	•	Tostadas – 3 fried tortillas with meat, lettuce, avocado, tomato, onion, cheese, sour cream — $10.95 | A La Carte – $3.95
	•	Chalupa – Fried flour tortilla with meat or vegetables, topped with lettuce, avocado, onion, tomato, queso fresco — $11.95

⸻

🌶️ Casa de las Enchiladas

All come with rice + beans unless noted.
	•	Enchiladas Roja – Chicken, salsa roja, lettuce, tomato, onion, avocado, queso fresco, sour cream — $14
	•	Enchiladas Verde – Chicken, salsa verde, melted cheese, sour cream, grilled cambrey onion, avocado, cilantro — $15
	•	Enchiladas Poblanas – Chicken, mole sauce, queso fresco, onions, sour cream — $14
Contains peanuts and sesame seeds
	•	Enchiladas Calabaza – Zucchini in roja, verde, or mole sauce, topped with lettuce, tomato, onion, avocado, queso fresco — $14
	•	Enchiladas al Horno – Chicken, green salsa, queso fresco, onion, sour cream, lettuce, tomato, avocado — $14
	•	Enchiladas Mixtas – 4 enchiladas with different sauces, served with grilled steak (no rice/beans) — $14.95

⸻

🌮 Tacos Auténticos

All include rice + beans unless noted.
	•	Tacos de Carne Asada – Grilled steak on corn tortillas with onion, cilantro, lime — $14
	•	Taco Gringo – Meat on flour tortilla with lettuce, tomato, queso fresco, sour cream — $14
	•	Tacos al Pastor – Pork marinated in guajillo chile with pineapple — $14
	•	Tacos de Pescado – Grilled or fried fish, cabbage slaw, chipotle sauce on flour tortillas — $14
	•	A La Carte Taco – Any taco — $5

Proteins Available:
Cabeza (Shredded Beef), Pollo, Carne Asada, Carne Molida, Al Pastor, Chorizo, Vegetariano, Camarones, Pescado

⸻

🔥 Fajitas

Served sizzling with onion, bell pepper, rice + beans, lettuce, tomato, avocado, and tortillas.
	•	Fajitas de Pollo – Chicken — $17 / $14.95
	•	Fajitas de Res – Steak — $18 / $15.95
	•	Fajitas de Camarón – Shrimp — $17 / $14.95
	•	Fajitas de Vegetales – Grilled veggies with lime — $14 / $11.95
	•	Fajitas Mixtas – Chicken, steak, and shrimp — $19 / $17.95

⸻

🐓 Pollo
	•	Pollo Asado – Marinated chicken with avocado, grilled onion, lettuce, tomato — $15
	•	Tinga de Pollo – Shredded chicken in chipotle and onion — $15
	•	Pollo en Mole – Chicken breast in mole sauce with sesame seed — $15
	•	Arroz con Pollo – Chicken with seasoned rice, avocado, tomato, onion, bell pepper (no rice/beans side) — $16

⸻

🥩 Carnes
	•	Carne Asada – Grilled steak with avocado, onion, lettuce, tomato — $16
	•	Bistec Encebollado – Grilled steak with grilled onion, jalapeño — $16
	•	Carne Enchilada – Steak in guajillo chile sauce with avocado, lettuce, tomato — $16
	•	Bistec a la Mexicana – Steak stewed in tomato, onion, jalapeño — $16
	•	Alambres – Steak with onion, bell pepper, bacon, and cheese — $16

⸻

🐟 Mariscos
	•	Shrimp Quesadilla – Quesadilla especial with shrimp — $17
	•	Camarones Guisados – Shrimp sautéed in garlic, mole or red sauce — $17
	•	Arroz con Camarón – Shrimp with seasoned rice, avocado, tomato, bell pepper (no rice/beans side) — $17

⸻

🌟 Specialty
	•	Quesabirria – 4 tacos with Birria and cheese, served with chili beef broth — $15
Rice and beans not included

⸻

🍽️ Sides
	•	Rice
	•	Beans
	•	Pico de Gallo
	•	Queso Fresco
	•	Sweet Plantains
	•	Avocado
	•	Sour Cream
	•	Tortillas
	•	To-Go Chips & Salsa — $2.49 or $3

⸻


<------------ End of restaurant menu ------------>
"""

sabor_promotional_calendar = """
Here is the promotional calendar for the Sabor Latin Street Grill restaurant:

<------------ Sabor Latin Street Grill promotional calendar ------------>

**Upcoming Restaurant Promotions: April - June 2025**

Get ready for some exciting deals and specials at our restaurant over the next few months! Here's a breakdown of our promotional calendar:

*   **April 9th - April 10th, 2025:** Loyalty Customers, enjoy a special treat! Get our delicious Cheese Quesadillas for just $4.49. (Available to Loyalty Customers only)
*   **April 18th - April 20th, 2025:** Planning a family meal? Our Email Subscribers will receive $5 off our Family Meal Boxes. (Available to Email Subscribers)
*   **April 27th, 2025:** We're reaching out with information about our great Value Meals specifically for customers we haven't seen in a while. (Targeting 3 Months Lapsed Customers)
*   **Around May 5th, 2025 (Preorder Dates TBD):** Celebrate Cinco de Mayo with us! We'll be offering PreOrder Packs perfect for your fiesta. Keep an eye out for the exact preorder dates! (Available to Everyone)
*   **May 7th - May 11th, 2025:** Give the gift of great food! Get $5 off when you purchase $25 worth of Gift Cards. (Available to Everyone)
*   **May 12th - May 18th, 2025:** Loyalty members, earn rewards faster! Get 100 bonus points with any purchase you make during this week. (Available to Loyalty Customers only)
*   **May 19th - May 25th, 2025:** We miss you! Customers who haven't visited in 3 months can enjoy a Buy One, Get One (BOGO) deal on our popular Quesabirria Value Meals. (Available to 3 Months Lapsed Customers)
*   **May 28th - June 1st, 2025:** Another perk for our loyal fans! Take $2 off any Value Meal purchase. (Available to Loyalty Customers only)
<------------ End of promotional calendar ------------>
"""

sabor_food_allergens = """
Here is the food allergens for the Sabor Latin Street Grill restaurant:

<------------ Sabor Latin Street Grill food allergens ------------>

**Sabor Latin Street Grill Allergen Information**

*Please note: This information is based on the provided chart (ID 202409). The chart indicates the restaurant aims to be Fish, Peanut, and Tree Nut free, however, Shellfish is present in some items. Always inform the staff of any allergies when ordering, as Sabor cannot guarantee the complete absence of allergens.*

**Street Food:**
*   **Arepa Tradicional:** Contains Eggs, Soybean, and Dairy.
*   **Gordita:** Contains Soybean and Dairy.
*   **Carne Asada Fries:** Contains Wheat, Soybean, and Dairy.
*   **Empanada:** Contains Wheat, Eggs, Soybean, and Dairy.
*   **Elote Loco:** Contains Eggs, Soybean, and Dairy.
*   **Quesabirria:** Contains Soybean and Dairy.

**Burrito:**
*   **Three Amigos Burrito:** Contains Wheat, Soybean, and Dairy.
*   **Sabor Especial Burrito:** Contains Wheat, Soybean, and Dairy.
*   **BYO Burrito:** Contains Wheat and Soybean (Dairy may be added depending on choices).

**Tacos:**
*   **Americano Tacos:** Contains Wheat, Soybean, and Dairy.
*   **Autentico Tacos:** Contains Soybean.
*   **Locos Tacos:** Contains Soybean.
*   **BYO Tacos:** Contains Soybean.
*   **Chimi Shrimp Tacos:** Contains Wheat, Soybean, Shellfish, and Dairy.

**Bowls:**
*   **BYO Bowl:** Does not contain listed allergens (Wheat, Eggs, Soybean, Fish, Shellfish, Dairy) based on the chart, though additions may change this.
*   **Soup:** Contains Soybean and Dairy.
*   **Taco Salad:** Contains Wheat, Soybean, and Dairy.
*   **Cuban Bowl:** Contains Soybean and Dairy.

**Quesadillas / Nachos:**
*   **Quesadillas:** Contains Wheat, Soybean, and Dairy.
*   **Sabor Nachos:** Contains Soybean and Dairy.

**Kids Menu:**
*   **Taco Americano (No Protein):** Contains Wheat, Soybean, and Dairy.
*   **Quesadilla (No Protein):** Contains Wheat, Soybean, and Dairy.
*   **Chicken Tenders:** Contains Wheat and Soybean.

**Desserts:**
*   **Churros:** Contains Wheat, Eggs, Soybean, and Dairy.
*   **Guava Empanadas:** Contains Wheat, Soybean, and Dairy.
*   **Vanilla Ice Cream:** Contains Soybean and Dairy.

**Sides:**
*   **Platanos Maduros:** Contains Soybean and Dairy.
*   **Yuca Fries:** Contains Eggs and Soybean.
*   **French Fries:** Contains Soybean.
*   **Refried Beans:** Contains Soybean.
*   **Black Beans:** Contains Soybean.
*   **Guacamole:** Does not contain listed allergens.
*   **Pico de Gallo:** Does not contain listed allergens.
*   **Quinoa Brown Rice:** Contains Soybean.
*   **Mexican Rice:** Contains Soybean.
*   **Queso:** Contains Dairy.
*   **Chips:** Contains Soybean.
*   **Chimichurri:** Contains Soybean.

**Proteins:**
*   **Shredded Chicken:** Does not contain listed allergens.
*   **Ground Beef:** Contains Wheat and Dairy.
*   **Grilled Steak:** Contains Wheat and Soybean.
*   **Grilled Chicken:** Contains Soybean.
*   **Barbacoa:** Contains Soybean.
*   **Al Pastor Pork:** Contains Soybean.
*   **Chorizo Sausage:** Contains Soybean.
*   **Grilled Shrimp:** Contains Soybean and Shellfish.
*   **Vegan Chorizo:** Contains Soybean.
*   **Grilled Veggies:** Contains Soybean.

**Salsas:**
*   **Mild Salsa:** Does not contain listed allergens.
*   **Arbol Salsa:** Contains Soybean.
*   **Verde Salsa:** Does not contain listed allergens.
*   **Green Monster Salsa:** Contains Soybean.
*   **Pineapple Habanero Salsa:** Does not contain listed allergens.
*   **Charred Habanero Salsa:** Contains Soybean.

**Disclaimer:** This allergen information is provided as a guide based on the chart. Sabor cannot guarantee the complete absence of these allergens in their restaurants due to shared cooking and preparation areas. Always inform the restaurant of your allergies.

<------------ End of Sabor Latin Street Grill food allergens ------------>
"""

sabor_daily_specials = """
Here is the daily specials for the Sabor Latin Street Grill restaurant:

<------------ Sabor Latin Street Grill daily specials ------------>
**Spice Up Your Week with Our Daily Specials!**

*   **Monday:** Beat the Monday blues with our hearty Three Amigos Burrito, served with a drink, for only $8.99! Pair it perfectly with refreshing $3 Mexican Beers.
*   **Tuesday:** Join us for Taco Tuesday! Feast on our authentic Tacos Autenticos at the amazing price of $1.49 each.
*   **Wednesday:** Bring the family! On Wednesdays, Kids Meals are just $0.99 when you purchase an adult meal (one discounted kids meal per adult meal).
*   **Thursday:** Get a taste of tradition! Enjoy our featured Arepa or Empanada special for $8.49. Thirsty? Sip on vibrant $6 Mojitos all day!
*   **Friday:** Cheers to Friday! Relax and unwind with cool, crisp $5 Craft Beers to start your weekend right.
*   **Saturday:** It's fiesta time! Enjoy our classic, tangy Margaritas for just $6 all day long.
*   **Sunday:** Sunday Funday, made easy! Take $5 Off our delicious and convenient Family Meal Boxes – perfect for sharing.

<------------ End of Sabor Latin Street Grill daily specials ------------>
"""

sabor_menu = """
Here is the menu for the Sabor Latin Street Grill restaurant:

<------------ Sabor Latin Street Grill menu ------------>
**Welcome to Sabor! Experience the Vibrant Flavors of Authentic Street Food & Mexican Favorites!**

Get ready for a culinary journey with our carefully crafted dishes, made with fresh ingredients and traditional recipes. From handheld delights to hearty bowls, there's something for everyone.

**Street Food Sensations:**

*   **Empanada ($4.99):** A golden-fried pocket of perfection! Choose your filling from savory Ground Beef, Shredded Chicken, Chorizo, Barbacoa, Grilled Veggies, or Black Bean, all nestled with cheese inside. Also available in a sweet Guava Pineapple version! Served with our signature Rosada sauce. *(Must Try!)*
*   **Quesabirria ($9.99):** Two delicious Birria Tacos loaded with cheese and served with a rich Chili Dipping Sauce for the ultimate flavor dunk! (G)
*   **Arepa ($6.49):** A classic Venezuelan delight! A warm, tender stuffed corn cake filled with cheese, your choice of protein, and drizzled with Rosada sauce.
*   **Carne Asada Fries ($10.99):** Indulge in crispy fries piled high with juicy Steak, melted Queso, fresh Pico de Gallo, creamy Guac, Cotija cheese, and a dollop of Sour Cream. *(Must Try!)*
*   **Elote Loco ($4.99):** Grilled corn on the cob slathered in creamy Mayo, tangy Cotija cheese, and a sprinkle of Chili Powder. A true street food classic! (V, G)
*   **Platanos Maduros ($4.99):** Sweet, fried plantains perfectly caramelized, topped with fresh Cilantro, Cotija cheese, and served with a side of cool Sour Cream. (V, G)
*   **Gordita ($6.99):** A satisfying stuffed corn cake packed with crisp Lettuce, juicy Tomato, Cotija cheese, Sour Cream, and your choice of Beans & Protein.

**Authentic Tacos:**

*   **Taco Autentico ($2.99):** Simple, traditional, and delicious! Your choice of protein on a warm Corn Tortilla, topped with fresh Cilantro, Onion, and a squeeze of Lime. *(Must Try!)*
*   **Taco Americano ($3.49):** A familiar favorite! Your choice of protein on a soft Flour Tortilla with crisp Lettuce, Tomato, and shredded Cheese.
*   **Chimi Shrimp Taco ($3.99):** Grilled Shrimp on a Flour Tortilla, topped with Lettuce, Tomato, Cotija cheese, Cilantro, and our zesty Chimichurri sauce.

**Hearty Bowls & Burritos:**

*   **Taco Salad ($10.49):** A crispy fried tortilla bowl filled with Mixed Greens, Pico de Gallo, Queso, Cotija cheese, Sour Cream, and your choice of Rice, Beans & Protein. (V, D options available)
*   **Cuban Bowl ($10.99):** A taste of the islands! Tender Barbacoa and Shredded Chicken served over Mexican Rice and Quinoa-Brown Rice blend, with Black Beans, Lime, sweet Fried Plantains, and Cilantro. (G) *(Must Try!)*
*   **Sabor Salad ($8.99):** A lighter, vibrant mix of Greens, Lettuce, Black Beans, Corn, Tomato, Onion, creamy Avocado, Chimichurri dressing, and crispy Tortilla Strips. Add your favorite protein! (V, G, D options available)
*   **Sabor Especial Burrito ($10.99):** A flavor-packed burrito stuffed with Queso, Lettuce, Sour Cream, Pico de Gallo, Guac, and your choice of Rice, Beans & Protein.
*   **Three Amigos Burrito ($8.99):** Your choice of Queso, Rice, Beans & Protein wrapped tightly in a warm tortilla. Simple and satisfying.
*   **Chicken Fajita Soup (S $3.99 / L $5.99):** A comforting soup with Grilled Chicken, Tomato, Onion, Pepper, Corn, crispy Tortilla Strips, and fresh Cilantro. (G)

**Nachos & Quesadillas:**

*   **Sabor Nachos ($10.99):** Crispy tortilla chips loaded with Queso, Lettuce, Sour Cream, Pico de Gallo, Guac, Cotija cheese, and your choice of Beans & Protein. Perfect for sharing!
*   **Sabor Quesadilla ($6.49):** A warm, folded tortilla filled with melted cheese. Add your favorite protein upon request! (V)

**--- MAKE IT YOUR WAY! ---**

Customize your perfect meal!

*   **Tacos ($3.49 each):** Choose your Tortilla, Protein, and load it up with your favorite Toppings: Tomato, Onion, Cheese, Cilantro, Lettuce, Pineapple, Jalapeno, Spicy Rosada, Chimichurri.
*   **Burritos & Bowls ($9.99):** Start with Rice & Beans, add your Protein, and finish with Desired Toppings: Tomato, Onion, Cheese, Cilantro, Lettuce, Corn off the cob, Queso, Pineapple, Jalapeno.
*   **Nachos ($9.99):** Choose your Beans & Protein, then pile on the Desired Toppings: Tomato, Onion, Cheese, Cilantro, Lettuce, Corn off the cob, Queso, Pineapple, Jalapeno.

**Choose Your Protein:**
*(Extra Charge for Premium Proteins)*

*   Chorizo Sausage (G, D)
*   Vegan Chorizo (V, G, D)
*   Grilled Veggies (V, G, D)
*   Black Beans (V, G, D)
*   Ground Beef (D)
*   Shredded Chicken (G)
*   Grilled Chicken (G, D)
*   Al Pastor Pork (G, D)
*   Barbacoa (G, D)
*   **Premium:** Grilled Steak (D)
*   **Premium:** Grilled Shrimp w/ Onions & Tomatoes (G, D)

**(V) = Vegetarian | (G) = Gluten Friendly | (D) = Dairy Free**

*We strive to provide accurate dietary information, but please inform your server of any allergies or dietary restrictions.*


**Value Meals - A Complete & Delicious Deal!**

*   **Empanada Meal:** Choose your favorite empanada filling, served as a complete meal with crispy tortilla chips, your choice of a side, and a refreshing drink. **$8.99**
*   **Quesabirria Meal:** Indulge in two savory Birria Tacos, packed with tender meat and cheese, served alongside their rich chili dipping sauce (consommé), chips, and a drink. A trendy favorite! **$11.99**
*   **Chicken Fajita Soup Meal:** Warm up with a generous large bowl of our hearty Chicken Fajita Soup, accompanied by chips, your choice of side, and a drink. Comfort in a bowl! **$10.99**

**Signature Cocktails - Sip & Unwind!**

*   **Mucho Sabor Margarita:** Our premium margarita featuring top-shelf Patron Tequila, Grand Marnier, and fresh lime. The ultimate indulgence! **$11.99**
*   **Sabor Margarita:** A classic blend of smooth 1800 Tequila, Grand Marnier, and zesty lime. Perfectly balanced. **$9.99**
*   **Amigos Margarita:** Our delightful house margarita with Tequila, Triple Sec, and lime. Simple, refreshing, and always a good choice. **$6.99**
*   **Cuban Mojito:** Transport yourself to the tropics with this invigorating mix of House Rum, fresh mint, lime, and a splash of lemon-lime soda. **$6.99**
*   **Paloma:** A bubbly and bright favorite featuring House Tequila, lime, and refreshing grapefruit soda. **$6.99**

**Sides - Perfect Additions to Any Meal!**

*(Note: Large (L) & Extra Large (XL) Guacamole, Queso, and Pico de Gallo automatically come with chips!)*

*   **Guacamole (V,G,D):** Freshly made, creamy avocado dip.
    *   S: $2.99 | L: $5.49 | XL: $10.49
*   **Queso (V,G):** Warm, melty cheese dip, perfect for dipping.
    *   S: $2.99 | L: $5.49 | XL: $10.49
*   **Pico de Gallo (V,G,D):** A vibrant mix of fresh diced tomatoes, onions, cilantro, and lime.
    *   S: $1.79 | L: $3.29 | XL: $6.29
*   **Sour Cream (V,G):** Cool and creamy topping.
    *   S: $1.29 | L: $2.29 | XL: $4.49
*   **Rice: Mexican / Quinoa-Brown (V,G,D):** Choose our seasoned Mexican rice or hearty Quinoa-Brown rice blend.
    *   S: $1.69 | L: $2.79 | XL: $5.29
*   **Beans: Refried / Black (V,G,D):** Your choice of classic creamy refried beans or whole black beans.
    *   S: $1.69 | L: $2.79 | XL: $5.29
*   **Yuca Fries (V,G,D):** Crispy fried yuca root – a delicious alternative to potato fries.
    *   L: $3.79
*   **Fries (V,G,D):** Classic crispy French fries.
    *   L: $3.79
*   **Chips (V,G,D):** Crunchy house-made tortilla chips.
    *   L: $1.79

*(V = Vegetarian, G = Gluten-Friendly, D = Dairy-Free - Please inform staff of any allergies)*

**Kids Meals - Little Amigos Favorites! $5.29**

*Perfectly portioned for smaller appetites. Includes choice of 1 Entree, 1 Side, and a Fountain Drink.*
*   **Entree Choices:** Kids Taco, Kids Chicken Tenders, Kids Quesadilla
*   **Side Choices:** Chips & Queso, Rice & Beans, 1/2 Corn on the Cob, Kids Fries

**Desserts - Sweet Endings!**

*   **Guava Pineapple Empanada (V):** A warm, flaky pastry filled with sweet guava and pineapple, dusted with cinnamon sugar, and served with a side of sour cream and lime. A tropical delight! **$4.99**
*   **Ice Cream (V,G):** Simple and sweet classic vanilla ice cream. **$1.99**
*   **Churros (V):** Warm, crispy churros coated in cinnamon sugar with a delicious caramel filling. **$4.99**

**Family Boxes - Share the Flavor! $43 (Feeds 4-6 People)**

*Perfect for gatherings, parties, or easy family dinners!*

*   **Taco Box:** Everything you need to build your own tacos!
    *   12 Flour or Corn Tortillas
    *   Tortilla Chips
    *   Queso, Guac, *or* Pico de Gallo
    *   Choice of 3 Proteins
    *   Choice of Refried *or* Black Beans
    *   Choice of Mexican *or* Quinoa Rice
    *   Choice of Salsa
*   **Nacho Box:** Build the ultimate nacho platter!
    *   Tortilla Chips
    *   Queso, Guac, Pico de Gallo & Sour Cream
    *   Choice of 3 Proteins
    *   Choice of Refried *or* Black Beans
    *   Choice of Salsa

**Unlimited Salsa Bar! - Find Your Perfect Heat!**

Explore our amazing selection of house-made salsas to complement your meal. From mild to fiery, discover your favorite!

*   **Mild:** Gentle flavor, minimal heat.
*   **Verde (🌶️):** Tangy tomatillo-based salsa with a mild kick.
*   **Arbol (🌶️🌶️):** Smoky heat from arbol chilies.
*   **Pineapple Habanero (🌶️🌶️🌶️):** Sweet and spicy tropical fusion.
*   **Green Monster (🌶️🌶️🌶️):** A unique blend with intense flavor and heat.
*   **Charred Habanero (🌶️🌶️🌶️🌶️):** Deep, smoky flavor with a serious habanero punch!
<------------ End of Sabor Latin Street Grill menu ------------>
"""