import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function SimpleMarketplace() {
  const [userType, setUserType] = useState(null);
  const [products, setProducts] = useState([
  {
    name: "Shoes",
    price: "999",
    image: "https://via.placeholder.com/150"
  },
  {
    name: "Watch",
    price: "1499",
    image: "https://via.placeholder.com/150"
  },
  {
    name: "Phone",
    price: "12999",
    image: "https://via.placeholder.com/150"
  },
  {
    name: "Headphones",
    price: "799",
    image: "https://via.placeholder.com/150"
  },
  {
    name: "Bag",
    price: "499",
    image: "https://via.placeholder.com/150"
  },
  {
    name: "Sunglasses",
    price: "299",
    image: "https://via.placeholder.com/150"
  }
]);
  const [imagePreview, setImagePreview] = useState("");
  const [form, setForm] = useState({ name: "", price: "", image: "" });

  const handleImage = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onloadend = () => {
      setForm({ ...form, image: reader.result });
      setImagePreview(reader.result);
    };
    reader.readAsDataURL(file);
  };

  const addProduct = () => {
    if (!form.name || !form.price || !form.image) {
      alert("Fill all fields + image");
      return;
    }

    setProducts([...products, form]);
    setForm({ name: "", price: "", image: "" });
    setImagePreview("");
  };

  // LOGIN SCREEN
  if (!userType) {
    return (
      <div className="flex h-screen items-center justify-center gap-6">
        <Button onClick={() => setUserType("seller")}>Login as Seller</Button>
        <Button onClick={() => setUserType("customer")}>Login as Customer</Button>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">

      {/* SELLER PANEL */}
      {userType === "seller" && (
        <Card className="p-4">
          <CardContent className="space-y-3">
            <h2 className="text-xl font-bold">Seller Panel</h2>

            <Input
              placeholder="Product Name"
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
            />

            <Input
              placeholder="Price"
              value={form.price}
              onChange={(e) => setForm({ ...form, price: e.target.value })}
            />

            <input type="file" onChange={handleImage} />

            {imagePreview && (
              <img
                src={imagePreview}
                alt="preview"
                className="h-24 rounded-xl"
              />
            )}

            <Button onClick={addProduct}>Add Product</Button>
          </CardContent>
        </Card>
      )}

      {/* CUSTOMER PANEL */}
      {userType === "customer" && (
        <div>
          <h2 className="text-xl font-bold mb-4">Products</h2>

          {products.length === 0 && <p>No products yet</p>}

          <div className="grid grid-cols-2 gap-4">
            {products.map((p, i) => (
              <Card key={i} className="p-3">
                <CardContent>
                  <img
                    src={p.image}
                    alt="product"
                    className="h-32 w-full object-cover rounded-xl mb-2"
                  />
                  <p className="font-semibold">{p.name}</p>
                  <p>₹ {p.price}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}

      {/* RESET BUTTON */}
      <Button onClick={() => setUserType(null)}>Logout</Button>
    </div>
  );
}
