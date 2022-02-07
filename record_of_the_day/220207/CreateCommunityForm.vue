<template>
  <div>
    <h1 style="margin-bottom: 30px; padding-bottom: 10px; border-bottom: 1px solid #979797;">
      팬 커뮤니티 등록
    </h1>
    <template>
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="name"
          :counter="10"
          :rules="nameRules"
          label="이름"
          solo
          required
        ></v-text-field>

        <v-text-field
          v-model="title"
          :counter="30"
          :rules="titleRules"
          label="제목"
          solo
          required
        ></v-text-field>

        <v-file-input
          accept="image/*"
          label="File input"
          outlined
          dense
        ></v-file-input>
        <div style="display: flex; justify-content: center;">
          <v-btn style="background-color: #979797; color: #FFFFFF; margin: 0 10px;">취소</v-btn>
          <v-btn @click="submit" style="background-color: #797BF8; color: #FFFFFF; margin: 0 10px;">등록</v-btn>
        </div>
      </v-form>
    </template>
  </div>
</template>

<script>
  export default {
    name: 'CreateCommunityForm',

    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || '이름은 필수입니다.',
        v => (v && v.length <= 10) || '이름은 10자 이하이어야 합니다.'
      ],
      title: '',
      titleRules: [
        v => !!v || '제목은 필수입니다.',
        v => (v && v.length <= 30) || '제목은 30자 이하이어야 합니다.'
      ],
    }),

    methods: {
      submit () {
        this.$v.$touch()
      },
    }
  }
</script>