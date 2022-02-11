<template>
  <div style="display: flex; flex-flow: column; align-items: center;">
    <v-card
      style="width: 1000px; margin-top: 50px;"
    >
      <div>
        {{ title }}
      </div>
      <div>
        {{ openDate }}
      </div>
      <div>
        미팅 안내사항!
      </div>
      <div>
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aliquid tempora dolores ullam dicta quibusdam, modi dignissimos eos,
        nam maxime odio aliquam enim commodi, id ipsum minima explicabo. Veniam, error minus.
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aliquid tempora dolores ullam dicta quibusdam, modi dignissimos eos,
        nam maxime odio aliquam enim commodi, id ipsum minima explicabo. Veniam, error minus.
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Aliquid tempora dolores ullam dicta quibusdam, modi dignissimos eos,
        nam maxime odio aliquam enim commodi, id ipsum minima explicabo. Veniam, error minus.
      </div>

      <v-text-field
        v-model="enterCode"
        label="입장 코드"
        solo
        required
      ></v-text-field>

      <v-btn
        @click="enterMeeting()"
        style="background-color: #797BF8; color: #FFFFFF;"
      >
        입장
      </v-btn>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'MeetingGuide',
  data: function() {
    return {
      meetingId: '',
      title: '팬미팅!',
      openDate: '2020.01.01 10:00',
      enterCode: '',
    }
  },
  methods:{
    enterMeeting: function () {
      const enterCodeItem = {
        enterCode: this.enterCode,
      }
      this.$axios({
        method: 'put',
        url: `http://localhost:8080/api/v1/meetings/${this.meetingId}/enter`,
        data: enterCodeItem,
      })
      .then(res => {
        console.log(res)
        if (res.data === "SUCCESS") {
          this.$router.push({name:'MeetingRoom', params:{ meetingId: this.meetingId }})
        }
      })
      .catch(err => {
        console.log(err.response.data)
        if (err.response.data === "MEETING ING") {
          alert('현재 팬미팅이 진행중입니다. 잠시만 기다려주세요.')
        } else if (err.response.data === "NO ENTER TWICE") {
          alert('팬미팅을 중복해서 들어갈 수 없습니다.')
        } else if (err.response.data === "MANAGER NOT IN") {
          alert('아직 팬미팅이 시작하지 않았습니다. 잠시만 기다려주세요.')
        } else if (err.response.data === "Wrong EnterCode") {
          alert('코드를 다시 확인해 주세요.')
        }
      })
      
    }
  },
  created: function () {
    this.meetingId = this.$route.params.meetingId

    this.$axios({
      method: 'get',
      url: `http://localhost:8080/api/v1/meetings/${this.meetingId}`,
    })
    .then(res => {
      this.title = res.data.title
      this.content = res.data.content
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>
