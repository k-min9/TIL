package com.example.mybatis.service;

import com.example.mybatis.dto.UseDataDto;
import com.example.mybatis.dto.UseListDto;
import com.example.mybatis.mapper.UseDataMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

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

        // 문자열 파싱
        for (UseListDto useListDto: lists) {
            List<String> tmpList = useListDto.getPay_method();
            if (tmpList != null) {
                String tmpString = tmpList.get(0);
                List<String> parsedString = Arrays.asList(tmpString.split(","));
                useListDto.setPay_method(parsedString);
            }
        }

        result.put("list2", lists);
        return result;
    }

    @Override
    public Map<String, Object> getUseListByPaymethodName(String paymethod) {
        Map<String, Object> result = new HashMap<>();
        List<UseListDto> lists = useDataMapper.getAllUseList();

        // paymethod가 있을 경우 필터용 리스트 생성
        List<String> filters = null;
        if (paymethod != null) {
            filters = Arrays.stream(paymethod.split(","))
                    .map(String::trim)
                    .collect(Collectors.toList());
        }

        // 이후 문자열 파싱하여 List로
        List<UseListDto> filteredList = new ArrayList<>();
        for (UseListDto useListDto: lists) {
            List<String> tmpList = useListDto.getPay_method();
            if (tmpList != null) {
                String tmpString = tmpList.get(0);
                List<String> parsedString = Arrays.asList(tmpString.split(","));
                System.out.println(parsedString);
                // 필터용리스트가 있고, 그 안에 내용이 포함되어있을 경우 다음 list로 이동
                if (filters!=null && !chkFilter(parsedString, filters)) continue;
                // 문제없으면 List 세팅하고 담기
                useListDto.setPay_method(parsedString);
                filteredList.add(useListDto);
            }
        }

        result.put("list3", filteredList);
        return result;
    }

    /**
     * A안에 필터와 겹치는 내용물이 하나라도 있으면 true, 없으면 false
     */
    public boolean chkFilter(List<String> listA, List<String> filters) {
        for (String strA : listA) {
            if (filters.contains(strA)) {
                return true;
            }
        }
        return false;
    }


}
