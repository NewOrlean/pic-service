<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal">
      <h3>Добавить картинку</h3>

      <label class="file-label">
        <span class="file-content">
          📁
          <span class="file-name">{{ fileName || "Выберите файл" }}</span>
        </span>
        <input type="file" @change="handleFileChange" ref="fileInput" />
      </label>

      <div v-if="preview" class="preview">
        <img :src="preview" alt="Preview" />
      </div>

      <textarea
        v-model="localDescription"
        placeholder="Описание"
        rows="4"
        class="modal-textarea"
      ></textarea>

      <div class="button-row">
        <button
          class="modal-button accept"
          @click="onSubmit"
          :disabled="loading"
        >
          Загрузить
        </button>
        <button
          class="modal-button cancel"
          @click="$emit('close')"
          :disabled="loading"
        >
          Отмена
        </button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ["fileName", "preview", "description", "loading"],
    emits: ["close", "submit", "file-change"],
    data() {
      return {
        localDescription: this.description || "",
      };
    },
    methods: {
      handleFileChange(event) {
        const file = event.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (e) => {
          this.$emit("file-change", {
            file,
            fileName: file.name,
            preview: e.target.result,
          });
        };
        reader.readAsDataURL(file);
      },
      onSubmit() {
        this.$emit("submit", { description: this.localDescription });
      },
    },
    watch: {
      description(val) {
        this.localDescription = val;
      },
    },
  };
</script>
