<template>
  <div class="pagination">
    <button @click="$emit('prev')" :disabled="page === 1 || loading">← Назад</button>
    <span>Страница {{ page }} из {{ totalPages }}</span>
    <button @click="$emit('next')" :disabled="page === totalPages || loading">Вперёд →</button>
  </div>
</template>

<script>
export default {
  name: 'ImagePagination',
  props: ['page', 'totalPages', 'loading'],
  emits: ['prev', 'next']
};
</script>
