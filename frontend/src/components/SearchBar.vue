<template>
  <div class="search-wrapper">
    <input class="search-input" type="text" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" placeholder="Поиск по описанию"/>
    <button class="search-button" @click="$emit('search')">🔍</button>
  </div>
</template>

<script>
export default {
  props: ['modelValue']
};
</script>
