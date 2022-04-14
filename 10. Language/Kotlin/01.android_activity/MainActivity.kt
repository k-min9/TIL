package com.example.sayhello

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts
import com.example.sayhello.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    val binding by lazy { ActivityMainBinding.inflate(layoutInflater) }

    lateinit var activityResultLauncher: ActivityResultLauncher<Intent>


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        binding.btnSay.setOnClickListener() {
            binding.textSay.text = "Hello Kotlin!"
        }

        // Activity 반환 정보를 받을 코드 : ActivityResultLauncher
        activityResultLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult())
        { result ->
            if (result.resultCode == RESULT_OK) {
                val message = result.data?.getStringExtra("returnValue")
                binding.resultText.text = message
                Toast.makeText(this, "안녕하세요, " + message + "님", Toast.LENGTH_SHORT).show()
            }
        }

        binding.btnMove.setOnClickListener{
            val intent = Intent(this, SubActivity::class.java)
            // 정보 전달
            intent.putExtra("from1", "Hello Bundle!!!")
            intent.putExtra("from2", 2022)
            //startActivityForResult(intent, 99)  // deprecated
            activityResultLauncher.launch(intent)
        }
    }
}