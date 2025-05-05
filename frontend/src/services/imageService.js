const backendUrl = process.env.VUE_APP_BACKEND_URL;

export async function uploadImage(data) {
  const res = await fetch(`${backendUrl}/upload_image`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  if (!res.ok) throw new Error('Ошибка при загрузке изображения');
  return res.json();
}

export async function getImages(page, pageSize, search) {
  const res = await fetch(`${backendUrl}/paginate_images?page=${page}&page_size=${pageSize}&search=${encodeURIComponent(search)}`);
  if (!res.ok) throw new Error('Ошибка при загрузке данных с сервера');
  return res.json();
}

export async function deleteImage(imageId) {
  const res = await fetch(`${backendUrl}/delete_image`, {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ image_id: imageId })
  });
  if (!res.ok) throw new Error('Ошибка при удалении изображения');
  return res.json();
}
