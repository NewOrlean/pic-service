<template>
  <div class="container">
    <div class="add-wrapper">
      <button class="add-button" @click="showUploadPopup = true">+ Добавить новую картинку</button>
      <div v-if="loading" class="add-inline-spinner"></div>
      <div v-if="error" class="error">{{ error }}</div>
    </div>

    <UploadModal
        v-if="showUploadPopup"
        :file-name="fileName"
        :preview="preview"
        :description="description"
        :loading="loading"
        @file-change="onFileChange"
        @close="closeUploadPopup"
        @submit="submitPicture"
    />

    <div class="search-wrapper">
      <input
          class="search-input"
          type="text"
          v-model="search"
          @input="onSearchInput"
          placeholder="Поиск по описанию"
      />
      <button class="search-button" @click="onSearch" title="Поиск">
        <svg xmlns="http://www.w3.org/2000/svg" class="search-icon" viewBox="0 0 24 24" fill="none"
             stroke="currentColor">
          <circle cx="11" cy="11" r="8"/>
          <line x1="21" y1="21" x2="16.65" y2="16.65"/>
        </svg>
      </button>
    </div>

    <div class="grid-wrapper">
      <div class="grid">
        <ImageCard
            v-for="image in images"
            :key="image.image_id"
            :image="image"
            @delete="deleteImage"
        />
      </div>
    </div>

    <div v-if="deleteMessage" class="delete-message">{{ deleteMessage }}</div>

    <ImagePagination
        :page="page"
        :totalPages="totalPages"
        :loading="loading"
        @prev="prevPage"
        @next="nextPage"
    />
  </div>
</template>

<script>
import UploadModal from '../components/UploadModal.vue';
import ImageCard from '../components/ImageCard.vue';
import ImagePagination from '../components/ImagePagination.vue';

export default {
  components: {UploadModal, ImageCard, ImagePagination},
  data() {
    return {
      file: null,
      fileName: '',
      preview: null,
      description: '',
      created_at: null,
      showUploadPopup: false,
      search: '',
      images: [],
      page: 1,
      totalPages: 1,
      pageSize: 6,
      loading: false,
      error: '',
      deleteMessage: ''
    };
  },
  mounted() {
    this.loadImages();
  },
  methods: {
    onFileChange({file, fileName, preview}) {
      this.file = file;
      this.fileName = fileName;
      this.preview = preview;
      this.created_at = new Date().toISOString();
    },
    formatDate(dateStr) {
      const date = new Date(dateStr);
      return date.toLocaleString();
    },
    async submitPicture({description}) {
      if (!this.preview || !description) {
        alert("Выберите файл и введите описание");
        return;
      }

      this.loading = true;
      this.error = "";

      try {
        const uploadRes = await fetch("http://localhost:8000/upload_image", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
            image: this.preview,
            description: description,
            created_at: this.created_at,
          }),
        });

        if (!uploadRes.ok) throw new Error("Ошибка при загрузке изображения.");

        this.closeUploadPopup();
        this.page = 1;
        await this.loadImages();
      } catch (err) {
        console.error("Ошибка при загрузке:", err);
        this.error = "Ошибка при загрузке изображения.";
        setTimeout(() => {
          this.error = "";
        }, 10000);
      } finally {
        this.loading = false;
      }
    },
    async loadImages() {
      this.loading = true;
      this.error = "";

      try {
        const res = await fetch(
            `http://localhost:8000/paginate_images?page=${this.page}&page_size=${this.pageSize}&search=${encodeURIComponent(this.search)}`
        );

        if (!res.ok) throw new Error("Ошибка при загрузке данных с сервера.");

        const data = await res.json();
        console.log("Загруженные данные:", data);

        this.images = data.images || [];
        this.totalPages = data.total_pages || 1;
      } catch (err) {
        console.error("Ошибка при получении изображений:", err);
        this.error = "Ошибка загрузки изображений";
        setTimeout(() => {
          this.error = "";
        }, 10000);
      } finally {
        this.loading = false;
      }
    },
    async deleteImage(imageId) {
      const confirmDelete = confirm("Удалить эту картинку?");
      if (!confirmDelete) return;

      this.loading = true;
      this.error = "";
      this.deleteMessage = "";

      try {
        const res = await fetch("http://localhost:8000/delete_image", {
          method: "DELETE",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({image_id: imageId}),
        });

        if (!res.ok) throw new Error("Ошибка при удалении изображения");

        const result = await res.json();
        this.deleteMessage = `Результат удаления: ${result.message}`;

        if (this.images.length === 1 && this.page > 1) {
          this.page--;
        }

        await this.loadImages();
      } catch (err) {
        console.error(err);
        this.error = "Ошибка при удалении изображения";
      } finally {
        this.loading = false;
        setTimeout(() => {
          this.deleteMessage = "";
        }, 3000);
      }
    },
    async nextPage() {
      if (this.page < this.totalPages && !this.loading) {
        this.loading = true;
        this.error = "";
        try {
          const nextPage = this.page + 1;
          const res = await fetch(
              `http://localhost:8000/paginate_images?page=${nextPage}&page_size=${this.pageSize}&search=${encodeURIComponent(this.search)}`
          );
          if (!res.ok) throw new Error("Ошибка при загрузке данных с сервера");
          const data = await res.json();
          this.images = data.images;
          this.totalPages = data.total_pages;
          this.page = nextPage;
        } catch (err) {
          console.error(err);
          this.error = "Ошибка загрузки изображений";
          setTimeout(() => {
          this.error = "";
        }, 10000);
        } finally {
          this.loading = false;
        }
      }
    },
    async prevPage() {
      if (this.page > 1 && !this.loading) {
        this.loading = true;
        this.error = "";
        try {
          const prevPage = this.page - 1;
          const res = await fetch(
              `http://localhost:8000/paginate_images?page=${prevPage}&page_size=${this.pageSize}&search=${encodeURIComponent(this.search)}`
          );
          if (!res.ok) throw new Error("Ошибка при загрузке данных с сервера");
          const data = await res.json();
          this.images = data.images;
          this.totalPages = data.total_pages;
          this.page = prevPage;
        } catch (err) {
          console.error(err);
          this.error = "Ошибка загрузки изображений";
          setTimeout(() => {
          this.error = "";
        }, 10000);
        } finally {
          this.loading = false;
        }
      }
    },
    onSearch() {
      this.page = 1;
      this.loadImages();
    },
    onSearchInput() {
      if (this.search === "") {
        this.page = 1;
        this.loadImages();
      }
    },
    closeUploadPopup() {
      this.showUploadPopup = false;
      this.description = "";
      this.preview = null;
      this.file = null;
      this.created_at = null;
      this.fileName = "";
    }
  }
};
</script>