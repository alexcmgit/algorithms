<p><a href="https://www.beecrowd.com.br/repository/UOJ_2742_en.html">beecrowd.com.br/repository/UOJ_2742_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2742 </span>
                                    <h1>Richard's Multiverse</h1>
                                    <div>
                                      <p>Marcos Lima <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>
                                    Richard is a famous scientist because of his multiverse theory, where he describes every hypothetical set of parallel universes by means of a database. Thanks to that you now have a job..</p>
                                    <p>
                                    As your first task, you must select every Richard from dimensions C875 and C774, together with its existence probability (the famous factor N) with three decimal places of precision.</p>
                                    <p>Remember that the N factor is calculated by multiplying the <b>omega</b> value by 1,618. The data must be sorted by the least <b>omega</b> value.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>dimensions</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>varchar</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>life_registry</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>name</td>
                              <td>varchar</td>
                            </tr>
                            <tr>
                              <td>omega</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>dimensions_id (FK)</td>
                              <td>numeric</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>dimensions</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>C774</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>C784</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>C794</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>C824</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>C875</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>life_registry</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>omega</strong></td>
                  <td><strong>dimensions_id</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Richard Postman</td>
                  <td>5.6</td>
                  <td>2</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Simple Jelly</td>
                  <td>1.4</td>
                  <td>1</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Richard Gran Master</td>
                  <td>2.5</td>
                  <td>1</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Richard Turing</td>
                  <td>6.4</td>
                  <td>4</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Richard Strall</td>
                  <td>1.0</td>
                  <td>3</td>
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
          <td><strong>The N Factor</strong></td>
        </tr>
        <tr>
          <td>Richard Gran Master</td>
          <td>4.045</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>