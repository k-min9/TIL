package com.example.sayhello

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.sayhello.databinding.ActivityMainBinding
import com.example.sayhello.databinding.ActivitySubBinding

class SubActivity : AppCompatActivity() {

    val binding by lazy { ActivitySubBinding.inflate(layoutInflater) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        // 위젯이 많을때는 with 스코프 쓰는게 편할수도 있음
        with(binding) {
            // 꺼내 쓸때는 타입지정을 해줘야함
            to1.text = intent.getStringExtra("from1")
            to2.text = "${intent.getIntExtra("from2", 0)}"  // 숫자를 꺼낸 후, 문자로 변환

            btnClose.setOnClickListener {
                val returnIntent = Intent()
                val message = editMessage.text.toString()
                returnIntent.putExtra("returnValue", message)
                setResult(Activity.RESULT_OK, returnIntent)
                finish()
            }
        }
    }
}