const BASE_URL = 'http://localhost:8000';

export async function uploadImage(data) {
  const res = await fetch(`${BASE_URL}/upload_image`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  if (!res.ok) throw new Error('Ошибка загрузки');
  return res.json();
}

export async function getImages(page, pageSize, search) {
  const res = await fetch(`${BASE_URL}/paginate_images?page=${page}&page_size=${pageSize}&search=${encodeURIComponent(search)}`);
  if (!res.ok) throw new Error('Ошибка загрузки');
  return res.json();
}

export async function deleteImage(imageId) {
  const res = await fetch(`${BASE_URL}/delete_image`, {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ image_id: imageId })
  });
  if (!res.ok) throw new Error('Ошибка удаления');
  return res.json();
}
