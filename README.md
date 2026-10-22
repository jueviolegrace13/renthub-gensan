# RentHub Gensan

Interactive website preview for **RentHub Gensan**, a multi-category equipment rental hub in General Santos City.

> Rent What You Need, The Smarter Choice Indeed.

## What's included

- **Storefront:** homepage, an equipment catalog with live availability by date (rental packages and individual items, filterable by category), and item details.
- **Customer flow:** sign up and log in, a multi-item cart, rental date selection and pickup-only checkout.
- **Customer dashboard:** reservation tracking, history and profile.
- **Admin console:** overview, reservations, equipment and inventory, a 14-day availability calendar and customers.
- **Release and check-in:** releasing equipment records the customer's ID, signed agreement, payment and inspection. Checking it in works out late-return charges, damage charges and the deposit refund.
- **Double-booking prevention:** pending, confirmed and picked-up reservations all hold stock, and the following are blocked whenever they would oversell a date:
  - checkout
  - restoring a cancelled reservation
  - lowering an item's stock

### Categories

| Category | Equipment |
|---|---|
| Events and Parties | Event Chairs, Event Tables, Sound System |
| Entertainment Equipment | Karaoke Machine, Board Games, Projector and Screen |
| Photography and Content Creation | DSLR Camera, Underwater Camera, Photography Reflector Set |
| Outdoor and Camping | Camping Tent, Folding Camping Chair, Folding Camping Table |
| Beach and Water Activities | Diving Fins, Diving Mask, Life Vest – Kids and Adults |

Rates, deposits, packages and stock follow the feasibility study (Tables 5, 6 and 22).

### Shop rules

- All reservations are picked up and returned at the shop on Pan-Philippine National Highway, Barangay City Heights. The site has no delivery or shipping options.
- The shop is open Monday to Saturday, 9:00 AM to 5:00 PM, and closed on Sundays, so pickups and returns can't fall on a Sunday.
- Each rental day is a 24-hour period from the pickup time. Short-term rentals run up to 6 days, and long-term rentals run 7 days and above.

## Preview accounts

| Role | Email | Password |
|---|---|---|
| Customer | juan@example.com | demo123 |
| Admin | admin@renthubgensan.ph | admin123 |

## Notes

- This is a front-end mockup. The data is sample data saved in the browser's `localStorage`, and there is no backend yet.
- The phone number, email and testimonials are placeholders.
- Prices, deposits and packages are set near the top of the script in `index.html` (`SEED_ITEMS` and `RENTAL_PACKAGES`). After changing a price, raise `PRICING_VERSION` by 1 so browsers load the new sample data.
- Rental packages are their own cart lines with fixed contents and the package rate. Anything added on top is an individual item at the regular rate, so a package's discount never grows with extra items. Loose items that make up a full package aren't discounted automatically; the cart offers to switch them to the package.
- Static site: open `index.html` directly, or deploy the folder to any static host (it's deployed on Vercel).
