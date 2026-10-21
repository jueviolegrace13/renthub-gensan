# RentHub GenSan

Interactive website preview for **RentHub GenSan**, a multi-category equipment rental hub in General Santos City.

> Rent What You Need, The Smarter Choice Indeed.

## What's included

- **Storefront:** homepage, an equipment catalog with live availability by date, and item details.
- **Customer flow:** sign up and log in, a multi-item cart, rental date selection and pickup-only checkout.
- **Customer dashboard:** reservation tracking, history and profile.
- **Admin console:** overview, reservations, equipment and inventory, a 14-day availability calendar and customers.
- **Double-booking prevention:** pending, confirmed and picked-up reservations all hold stock, and the following are blocked whenever they would oversell a date:
  - checkout
  - restoring a cancelled reservation
  - lowering an item's stock

### Categories

| Category | Equipment |
|---|---|
| Events & Parties | Event Chairs, Event Tables, Sound System |
| Entertainment | Karaoke Machine, Board Games, Projector and Screen |
| Photography | DSLR Camera, Underwater Camera, Photography Reflector Set |
| Outdoor & Camping | Camping Tent, Folding Camping Chair, Folding Camping Table |
| Beach & Water | Swim/Diving Fins, Diving Mask, Life Vest – Kids and Adults |

All reservations are picked up at the physical shop. The site has no delivery or shipping options.

## Preview accounts

| Role | Email | Password |
|---|---|---|
| Customer | juan@example.com | demo123 |
| Admin | admin@renthubgensan.ph | admin123 |

## Notes

- This is a front-end mockup. The data is sample data saved in the browser's `localStorage`, and there is no backend yet.
- The address, phone number and testimonials are placeholders. Equipment rates and refundable deposits are configured in the catalog data in `index.html`.
- Static site: open `index.html` directly, or deploy the folder to any static host (it's deployed on Vercel).
