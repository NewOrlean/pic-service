<template>
  <div class="card">
    <img :src="image.image_url" alt="image" />
    <p class="description" :title="image.description">{{ image.description }}</p>
    <div class="card-footer">
      <span class="created-at">📅 {{ formatDate(image.created_at) }}</span>
      <button class="delete-icon" @click="$emit('delete', image.image_id)" title="Удалить">
        <svg xmlns="http://www.w3.org/2000/svg" class="trash-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M9 7V4h6v3m-9 0h12"/>
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['image'],
  emits: ['delete'],
  methods: {
    formatDate(dateStr) {
      const date = new Date(dateStr);
      return date.toLocaleString();
    }
  }
};
</script>
