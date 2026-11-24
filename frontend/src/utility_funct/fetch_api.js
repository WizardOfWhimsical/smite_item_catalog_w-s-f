const BASE_URL = "/v1/api/py_backend";

export async function get_items() {
  try {
    const response = await fetch(BASE_URL);
    if (!response.ok) {
      throw new Error("Response for item list not ok.");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    return { message: error.message };
  }
}
export async function post_item(item) {
  try {
    const response = await fetch(BASE_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(item),
    });

    if (!response.ok) {
      throw new Error("Response from backend failed, check logs");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    return { message: error.message };
  }
}
