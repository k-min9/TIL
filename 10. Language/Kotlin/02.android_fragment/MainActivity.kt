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

    val listFragment by lazy {ListFragment()}
    val detailFragment by lazy {ListFragment()}

    lateinit var activityResultLauncher: ActivityResultLauncher<Intent>


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        setFragment()


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

    fun setFragment() {
        // 1. 사용할 프래그먼트 생성 >> 위에 생성해도 좋음
//            val listFragment = ListFragment()
        // 2. 트랜잭션 생성
        val transaction = supportFragmentManager.beginTransaction()
        // 3. 트랜잭션을 통해 프래그먼트 삽입
        transaction.add(R.id.fragTest, listFragment)
        transaction.commit()
    }

    fun goDetail() {
        val transaction = supportFragmentManager.beginTransaction()
        transaction.add(R.id.fragTest, detailFragment)
        // 트랜 잭션 동작을 스택에 저장.
        // 뒤로 가기시 스택에 있는 프래그먼트 들이 순서대로 onDestroy
        transaction.addToBackStack("detail")
        transaction.commit()
    }
    fun goBack() {
        onBackPressed()
    }

}