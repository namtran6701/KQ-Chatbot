from datetime import datetime
today_date = datetime.now().strftime("%Y-%m-%d") 

brand_tone = f"""
Here is brand tone that you should follow when responding to customer reviews:
<------------ Begin of response tone ------------>
You are the brand ambassador and official voice of our restaurant. When responding to customer reviews, follow these rules:

Today's date is {today_date}.

1. **Voice and Tone**  
   - Always be warm, friendly, and authentic—like a welcoming host.  
   - Use the customer’s name if available.  
   - Refer to specific details (such as menu items, the atmosphere, or the exact location mentioned by the reviewer).

2. **Uniqueness**  
   - Every response should feel personal and unique to the individual review.  
   - If the review is in Spanish, respond in Spanish to reinforce our authentic Latin experience.

3. **Encouragement to Return**  
   - Invite the customer back on every positive or neutral interaction.  
   - Express excitement and eagerness to serve them again.

4. **Handling Different Star Ratings**  
   - **Positive Reviews (4–5 Stars)**  
     - Start with a friendly greeting and gratitude.  
     - Acknowledge any highlights (e.g., specific dishes, service).  
     - Reaffirm how happy we are that they enjoyed their experience.  
     - Invite them to visit again soon.
   - **Reviews With No Comment**  
     - If 4–5 Stars: Thank them simply and invite them back.  
     - If 1–3 Stars: Apologize, express regret that we missed the mark, request more details via email, and invite them to return so we can make it right.
   - **Negative Reviews (1–3 Stars or Specific Complaints)**  
     - Offer a sincere apology and acknowledge their concerns.  
     - Encourage them to reach out via our provided email (e.g., rosa@raydalhospitality.com) for further resolution.  
     - Mention you’d like to offer something special or a second chance to demonstrate the service and flavors we’re known for.

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
Here is the extracted information from the new screenshot as plain text:

---

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

promotional_calendar = """
Here is the promotional calendar for the restaurant:

<------------ promotional calendar ------------>

## 🌮 **Three Amigos Promotional Calendar**

### **January - "New Year, New Flavors"**
- **Promo**: "Enchiladas Fiesta" – 15% off all enchiladas.
- **Event**: *Three Kings Day* special with complimentary *Rosca de Reyes* slice (Jan 6).
- **Social Theme**: Showcase regional Mexican traditions and comfort dishes for the cold season.

---

### **February - "Amigos y Amor"**
- **Promo**: Couple's Combo – Shared Dip Trio, 2 Platos Tradicionales, and dessert for $35.
- **Event**: *Valentine’s Day Dinner* with live music and a complimentary appetizer.
- **Special Feature**: Spotlight on *Mole* dishes (Enchiladas Poblanas, Pollo en Mole).

---

### **March - "Taste of Spring"**
- **Promo**: Fresh Guacamole & Queso Fundido special – Free small guac with any fajitas.
- **Event**: *National Tortilla Chip Day* (March 23) – Free chips & salsa with any order.
- **Social Theme**: Lighter dishes, fish tacos, and shrimp specials.

---

### **April - "Cantina Season Kickoff"**
- **Promo**: "Taco Tour" – Mix & match 3 tacos + drink for $15.
- **Event**: *Spring Patio Opening Party* with live mariachi and happy hour deals.
- **Highlight**: Authentic *Tacos Auténticos* and *Quesabirria*.

---

### **May - "Cinco de Mayo Festival"**
- **Promo**: Full-week celebration with discounts on *Margaritas*, *Nachos Supreme*, and *Fajitas*.
- **Event**: Live bands, giveaways, and street food stalls.
- **Social Theme**: Vibrant, festive, and family-friendly.

---

### **June - "Summer Sizzlers"**
- **Promo**: Fajitas Month – 10% off all *Fajitas*.
- **Event**: *Father’s Day* Grill Special – Complimentary appetizer for dads.
- **Special Feature**: Launch seasonal drinks like *Agua Frescas* and *Frozen Margaritas*.

---

### **July - "Mexican Summer Nights"**
- **Promo**: $5 *A La Carte Tacos* all month.
- **Event**: *Patio Fiesta Fridays* with DJ, dance floor, and happy hour.
- **Social Theme**: Street food vibes, light bites, and refreshing drinks.

---

### **August - "Back to School, Back to Amigos"**
- **Promo**: Family Special – Free kid’s meal with purchase of 2 adult entrees.
- **Event**: *End of Summer Fiesta* with taco-eating contest.
- **Highlight**: Promote family-friendly dishes like *Tostadas* and *Quesadillas*.

---

### **September - "Viva Mexico!"**
- **Promo**: 2-for-1 Tacos on *Mexican Independence Day* (Sept 16).
- **Event**: Full weekend celebration with traditional dishes and performances.
- **Menu Focus**: Highlight regional dishes (*Tinga de Pollo*, *Chiles en Nogada* if available).

---

### **October - "Fall Flavors & Día de los Muertos"**
- **Promo**: Special *Mole Festival* – Try all dishes with mole sauce at a discount.
- **Event**: *Día de los Muertos* (Nov 1–2) – Decor, altars, and themed menu.
- **Social Theme**: Storytelling, traditions, and warm comforting dishes.

---

### **November - "Gracias, Amigos"**
- **Promo**: *Friendsgiving Fiesta* – Shared platters for groups at special prices.
- **Event**: *Thanksgiving Weekend* - Give thanks with special *Pollo Asado* and *Carnes* platters.
- **Community**: Collaborate with local food banks or run a canned food drive.

---

### **December - "Holiday Fiesta"**
- **Promo**: *Tamales* and *Ponche* holiday specials.
- **Event**: *Las Posadas* (Dec 16-24) – Traditional Mexican Christmas celebration.
- **Menu Feature**: Warm drinks, sweet plantains, and festive dishes.

---

<------------ End of promotional calendar ------------>
"""



