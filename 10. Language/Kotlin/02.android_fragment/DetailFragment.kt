package com.example.sayhello

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.sayhello.databinding.FragmentDetailBinding

// ListFragment와 거의 형태가 유사
class DetailFragment : Fragment() {
    
    lateinit var binding: FragmentDetailBinding
    lateinit var mainActivity: MainActivity
    
    override fun onAttach(context: Context) {
        super.onAttach(context)
        if(context is MainActivity) mainActivity = context
    }
    
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentDetailBinding.inflate(inflater, container, false)
        return binding.root
    }
    
    // 생명주기 상 다 만들어지고 리스너 붙이기 
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        binding.btnBack.setOnClickListener {
            mainActivity.goBack()
        }
    }
}