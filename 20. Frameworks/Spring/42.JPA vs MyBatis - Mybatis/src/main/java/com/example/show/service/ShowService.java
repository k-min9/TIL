package com.example.show.service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Service;

import com.example.show.dto.ShowDetailDto;
import com.example.show.dto.ShowDto;
import com.example.show.mapper.ShowMapper;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class ShowService {

  private final ShowMapper showMapper;
 
  public ShowDto getShowData(String user_no, String start_dt) {
    ShowDto result = showMapper.getShowData(user_no, start_dt);
    
    return result;  
  }

  public Map<String, Object> getShowList(String user_no, String start_dt) {
    Map<String, Object> result = new HashMap<>();

    List<ShowDetailDto> lists = showMapper.getShowList(user_no, start_dt);
    result.put("list", lists);

    return result;
  }
}
