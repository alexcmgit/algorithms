<p><a href="https://www.beecrowd.com.br/repository/UOJ_2738_en.html">beecrowd.com.br/repository/UOJ_2738_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2738 </span>
                                    <h1>Contest</h1>
                                    <div>
                                      <p>Marcos Lima <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>
                                    The Mars Technology University has Open Positions for researchers. However, the computer responsible for processing the candidates' data is broken. You must present the candidate list, containing the name and final score (with two decimal places of precision) of each candidate. Remember to show the list ordered by score (highest first).</p>
                                    <p>
                                    The score is given by the weighted average described as:</p>
                                    <p><span>\(Avg = \frac{(math * 2) + (specific * 3) + (project\_plan * 5)}{ 10}\)</span></p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>candidate</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>integer</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>varchar</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>score</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>candidate_id (FK)</td>
                              <td>integer</td>
                            </tr>
                            <tr>
                              <td>math</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>specific</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>project_plan</td>
                              <td>numeric</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>candidate</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Michael P Cannon</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Barbra J Cable</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Ronald D Jones</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Timothy K Fitzsimmons</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Ivory B Morrison</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Sheila R Denis</td>
                    </tr>
                    <tr>
                      <td>7</td>
                      <td>Edward C Durgan</td>
                    </tr>
                    <tr>
                      <td>8</td>
                      <td>William K Spencer</td>
                    </tr>
                    <tr>
                      <td>9</td>
                      <td>Donna D Pursley</td>
                    </tr>
                    <tr>
                      <td>10</td>
                      <td>Ann C Davis</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>score</caption>
                  <tbody><tr>
                  <td><strong>candidate_id</strong></td>
                  <td><strong>math</strong></td>
                  <td><strong>specific</strong></td>
                  <td><strong>project_plan</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>76</td>
                  <td>58</td>
                  <td>21</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>4</td>
                  <td>5</td>
                  <td>22</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>15</td>
                  <td>59</td>
                  <td>12</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>41</td>
                  <td>42</td>
                  <td>99</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>22</td>
                  <td>90</td>
                  <td>9</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>82</td>
                  <td>77</td>
                  <td>15</td>
                </tr>
                <tr>
                  <td>7</td>
                  <td>82</td>
                  <td>99</td>
                  <td>56</td>
                </tr>
                <tr>
                  <td>8</td>
                  <td>11</td>
                  <td>4</td>
                  <td>22</td>
                </tr>
                <tr>
                  <td>9</td>
                  <td>16</td>
                  <td>29</td>
                  <td>94</td>
                </tr>
                <tr>
                  <td>10</td>
                  <td>1</td>
                  <td>7</td>
                  <td>59</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
          <td><strong>avg</strong></td>
        </tr>
        <tr>
          <td>Edward C Durgan</td>
          <td>74.10</td>
        </tr>
        <tr>
          <td>Timothy K Fitzsimmons</td>
          <td>70.30</td>
        </tr>
        <tr>
          <td>Donna D Pursley</td>
          <td>58.90</td>
        </tr>
        <tr>
          <td>Sheila R Denis</td>
          <td>47.00</td>
        </tr>
        <tr>
          <td>Michael P Cannon</td>
          <td>43.10</td>
        </tr>
        <tr>
          <td>Ivory B Morrison</td>
          <td>35.90</td>
        </tr>
        <tr>
          <td>Ann C Davis</td>
          <td>31.80</td>
        </tr>
        <tr>
          <td>Ronald D Jones</td>
          <td>26.70</td>
        </tr>
        <tr>
          <td>William K Spencer</td>
          <td>14.40</td>
        </tr>
        <tr>
          <td>Barbra J Cable</td>
          <td>13.30</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>