const BASE_URL = "/v1/api/py_backend";

export async function get_items() {
  const response = await fetch(BASE_URL);

  if (!response.ok) {
    return { message: "Response not ok" };
  }

  const data = await response.json();

  return data;
}
