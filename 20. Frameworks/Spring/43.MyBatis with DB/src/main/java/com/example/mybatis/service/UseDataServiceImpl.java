package com.example.mybatis.service;

import com.example.mybatis.dto.UseDataDto;
import com.example.mybatis.dto.UseListDto;
import com.example.mybatis.mapper.UseDataMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class UseDataServiceImpl implements UseDataService{

    private final UseDataMapper useDataMapper;
    @Override
    public UseDataDto getUseData(String user_no, String start_dt) {
        return useDataMapper.getUseData(user_no, start_dt);
    }

    @Override
    public Map<String, Object> getUseList(String user_no, String start_dt) {
        Map<String, Object> result = new HashMap<>();
        List<UseListDto> lists = useDataMapper.getUseList(user_no, start_dt);
        result.put("list", lists);
        return result;
    }

    @Override
    public Map<String, Object> getUseList2(String user_no, String start_dt) {
        Map<String, Object> result = new HashMap<>();
        List<UseListDto> lists = useDataMapper.getUseList2(user_no, start_dt);
        result.put("list2", lists);
        return result;
    }
}
