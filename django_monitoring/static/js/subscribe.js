function mediumRegion_add_all_select_option() {
  // '전체선택'의 pk값 구하기
  var all_select_pk = -1;
  const all_select = "전체선택";
  for (var i = mediums.length - 1; i >= 0; i--) {
    if (mediums[i].fields.name == all_select) {
      all_select_pk = mediums[i].pk;
    }
  }
  jQuery('#select-medium').append(fn_option(all_select_pk, all_select)); // '전체선택' 옵션 추가
}

function fn_option(code, name) {
  return '<option value="' + code + '">' + name + '</option>';
}
